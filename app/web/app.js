const formatCurrency = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
});

const rowsMetric = document.querySelector("#rowsMetric");
const unitsMetric = document.querySelector("#unitsMetric");
const revenueMetric = document.querySelector("#revenueMetric");
const averageMetric = document.querySelector("#averageMetric");
const salesTable = document.querySelector("#salesTable");
const productList = document.querySelector("#productList");
const statusText = document.querySelector("#statusText");
const productFilter = document.querySelector("#productFilter");
const regionFilter = document.querySelector("#regionFilter");
const applyFilters = document.querySelector("#applyFilters");

function buildQuery() {
  const params = new URLSearchParams();

  if (productFilter.value.trim()) {
    params.set("product", productFilter.value.trim());
  }

  if (regionFilter.value) {
    params.set("region", regionFilter.value);
  }

  return params.toString();
}

async function getJson(path) {
  const response = await fetch(path);

  if (!response.ok) {
    throw new Error(`Error HTTP ${response.status}`);
  }

  return response.json();
}

function renderSummary(summary) {
  rowsMetric.textContent = summary.rows;
  unitsMetric.textContent = summary.total_units;
  revenueMetric.textContent = formatCurrency.format(summary.total_revenue);
  averageMetric.textContent = formatCurrency.format(summary.average_sale);
}

function renderSalesTable(sales) {
  if (!sales.length) {
    salesTable.innerHTML = `
      <tr>
        <td colspan="6" class="empty-state">No hay ventas para estos filtros.</td>
      </tr>
    `;
    return;
  }

  salesTable.innerHTML = sales
    .map(
      (sale) => `
        <tr>
          <td>${sale.date}</td>
          <td>${sale.product}</td>
          <td>${sale.category}</td>
          <td>${sale.region}</td>
          <td>${sale.units}</td>
          <td>${formatCurrency.format(sale.total)}</td>
        </tr>
      `,
    )
    .join("");
}

function renderProductRanking(products) {
  if (!products.length) {
    productList.innerHTML = `<p class="empty-state">Sin resultados.</p>`;
    return;
  }

  const maxRevenue = Math.max(...products.map((item) => item.revenue));

  productList.innerHTML = products
    .map((item) => {
      const width = maxRevenue ? (item.revenue / maxRevenue) * 100 : 0;

      return `
        <div class="ranking-row">
          <div class="ranking-meta">
            <span>${item.product}</span>
            <span>${formatCurrency.format(item.revenue)}</span>
          </div>
          <div class="bar" aria-hidden="true">
            <span style="width: ${width}%"></span>
          </div>
        </div>
      `;
    })
    .join("");
}

async function loadDashboard() {
  const query = buildQuery();
  const suffix = query ? `?${query}` : "";
  statusText.textContent = "Cargando";

  try {
    const [summary, sales, products] = await Promise.all([
      getJson(`/api/sales/summary${suffix}`),
      getJson(`/api/sales${suffix}${suffix ? "&" : "?"}limit=25`),
      getJson(`/api/sales/by-product${suffix}`),
    ]);

    renderSummary(summary);
    renderSalesTable(sales);
    renderProductRanking(products);
    statusText.textContent = `${sales.length} filas`;
  } catch (error) {
    statusText.textContent = "Error";
    salesTable.innerHTML = `
      <tr>
        <td colspan="6" class="empty-state">${error.message}</td>
      </tr>
    `;
    productList.innerHTML = `<p class="empty-state">No se pudieron cargar los datos.</p>`;
  }
}

applyFilters.addEventListener("click", loadDashboard);
productFilter.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    loadDashboard();
  }
});

loadDashboard();


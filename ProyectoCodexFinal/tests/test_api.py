from fastapi.testclient import TestClient

from ProyectoCodexFinal.app.main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_sales_summary_has_totals() -> None:
    response = client.get("/api/sales/summary")

    assert response.status_code == 200
    data = response.json()
    assert data["rows"] == 20
    assert data["total_units"] > 0
    assert data["total_revenue"] > 0


def test_sales_can_be_filtered_by_region() -> None:
    response = client.get("/api/sales", params={"region": "Madrid"})

    assert response.status_code == 200
    data = response.json()
    assert data
    assert {sale["region"] for sale in data} == {"Madrid"}


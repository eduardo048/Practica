from dataclasses import dataclass

import pandas as pd

from ProyectoCodexFinal.app.core.config import Settings


REQUIRED_COLUMNS = {
    "sale_id",
    "date",
    "product",
    "category",
    "units",
    "unit_price",
    "region",
}


@dataclass
class SalesService:
    settings: Settings

    def _read_dataframe(self) -> pd.DataFrame:
        df = pd.read_csv(self.settings.data_file, parse_dates=["date"])
        missing_columns = REQUIRED_COLUMNS.difference(df.columns)

        if missing_columns:
            columns = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {columns}")

        df["units"] = pd.to_numeric(df["units"])
        df["unit_price"] = pd.to_numeric(df["unit_price"])
        df["total"] = df["units"] * df["unit_price"]
        return df.sort_values("date", ascending=False)

    def _filtered_dataframe(
        self,
        product: str | None = None,
        region: str | None = None,
    ) -> pd.DataFrame:
        df = self._read_dataframe()

        if product:
            df = df[df["product"].str.contains(product, case=False, na=False)]

        if region:
            df = df[df["region"].str.lower() == region.lower()]

        return df

    def list_sales(
        self,
        product: str | None = None,
        region: str | None = None,
        limit: int = 100,
    ) -> list[dict]:
        df = self._filtered_dataframe(product=product, region=region).head(limit).copy()
        df["date"] = df["date"].dt.date

        records = []
        for row in df.to_dict(orient="records"):
            row["sale_id"] = int(row["sale_id"])
            row["units"] = int(row["units"])
            row["unit_price"] = round(float(row["unit_price"]), 2)
            row["total"] = round(float(row["total"]), 2)
            records.append(row)

        return records

    def get_summary(
        self,
        product: str | None = None,
        region: str | None = None,
    ) -> dict:
        df = self._filtered_dataframe(product=product, region=region)
        rows = len(df)
        total_revenue = float(df["total"].sum())

        return {
            "rows": rows,
            "total_units": int(df["units"].sum()),
            "total_revenue": round(total_revenue, 2),
            "average_sale": round(total_revenue / rows, 2) if rows else 0,
        }

    def get_sales_by_product(
        self,
        product: str | None = None,
        region: str | None = None,
    ) -> list[dict]:
        df = self._filtered_dataframe(product=product, region=region)
        grouped = (
            df.groupby("product", as_index=False)
            .agg(units=("units", "sum"), revenue=("total", "sum"))
            .sort_values("revenue", ascending=False)
        )

        return [
            {
                "product": str(row["product"]),
                "units": int(row["units"]),
                "revenue": round(float(row["revenue"]), 2),
            }
            for row in grouped.to_dict(orient="records")
        ]

    def get_sales_by_region(
        self,
        product: str | None = None,
        region: str | None = None,
    ) -> list[dict]:
        df = self._filtered_dataframe(product=product, region=region)
        grouped = (
            df.groupby("region", as_index=False)
            .agg(units=("units", "sum"), revenue=("total", "sum"))
            .sort_values("revenue", ascending=False)
        )

        return [
            {
                "region": str(row["region"]),
                "units": int(row["units"]),
                "revenue": round(float(row["revenue"]), 2),
            }
            for row in grouped.to_dict(orient="records")
        ]


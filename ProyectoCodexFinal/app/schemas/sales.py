from datetime import date

from pydantic import BaseModel, Field


class Sale(BaseModel):
    sale_id: int
    date: date
    product: str
    category: str
    units: int = Field(ge=0)
    unit_price: float = Field(ge=0)
    region: str
    total: float = Field(ge=0)


class SalesSummary(BaseModel):
    rows: int
    total_units: int
    total_revenue: float
    average_sale: float


class ProductSales(BaseModel):
    product: str
    units: int
    revenue: float


class RegionSales(BaseModel):
    region: str
    units: int
    revenue: float


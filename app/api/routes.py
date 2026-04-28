from fastapi import APIRouter, Depends, Query

from app.core.config import Settings, get_settings
from app.schemas.sales import ProductSales, RegionSales, Sale, SalesSummary
from app.services.sales_service import SalesService


router = APIRouter(tags=["sales"])


def get_sales_service(settings: Settings = Depends(get_settings)) -> SalesService:
    return SalesService(settings=settings)


@router.get("/health")
def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {
        "status": "ok",
        "data_file": str(settings.data_file),
    }


@router.get("/sales", response_model=list[Sale])
def list_sales(
    product: str | None = None,
    region: str | None = None,
    limit: int = Query(default=100, ge=1, le=1000),
    service: SalesService = Depends(get_sales_service),
) -> list[dict]:
    return service.list_sales(product=product, region=region, limit=limit)


@router.get("/sales/summary", response_model=SalesSummary)
def sales_summary(
    product: str | None = None,
    region: str | None = None,
    service: SalesService = Depends(get_sales_service),
) -> dict:
    return service.get_summary(product=product, region=region)


@router.get("/sales/by-product", response_model=list[ProductSales])
def sales_by_product(
    product: str | None = None,
    region: str | None = None,
    service: SalesService = Depends(get_sales_service),
) -> list[dict]:
    return service.get_sales_by_product(product=product, region=region)


@router.get("/sales/by-region", response_model=list[RegionSales])
def sales_by_region(
    product: str | None = None,
    region: str | None = None,
    service: SalesService = Depends(get_sales_service),
) -> list[dict]:
    return service.get_sales_by_region(product=product, region=region)


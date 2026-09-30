from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.brand import (
    BrandCreate,
    BrandResponse,
    BrandUpdate,
)
from app.services import brand_service


router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.post(
    "/",
    response_model=BrandResponse,
    status_code=status.HTTP_201_CREATED
)
def create_brand(
    data: BrandCreate,
    db: Session = Depends(get_db)
):
    return brand_service.create_brand(db, data)


@router.get(
    "/",
    response_model=list[BrandResponse]
)
def list_brands(
    db: Session = Depends(get_db)
):
    return brand_service.list_brands(db)


@router.get(
    "/{brand_id}",
    response_model=BrandResponse
)
def get_brand(
    brand_id: int,
    db: Session = Depends(get_db)
):
    return brand_service.get_brand(db, brand_id)


@router.patch(
    "/{brand_id}",
    response_model=BrandResponse
)
def update_brand(
    brand_id: int,
    data: BrandUpdate,
    db: Session = Depends(get_db)
):
    return brand_service.update_brand(
        db,
        brand_id,
        data
    )


@router.delete(
    "/{brand_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db)
):
    brand_service.delete_brand(db, brand_id)
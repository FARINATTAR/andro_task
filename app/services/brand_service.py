from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.schemas.brand import BrandCreate, BrandUpdate


def create_brand(db: Session, data: BrandCreate):
    existing_brand = db.scalar(
        select(Brand).where(
            (Brand.name == data.name) | (Brand.slug == data.slug)
        )
    )

    if existing_brand:
        raise HTTPException(
            status_code=409,
            detail="Brand with this name or slug already exists"
        )

    brand = Brand(**data.model_dump())

    db.add(brand)
    db.commit()
    db.refresh(brand)

    return brand


def list_brands(db: Session):
    return db.scalars(
        select(Brand).where(Brand.is_deleted == False)
    ).all()


def get_brand(db: Session, brand_id: int):
    brand = db.scalar(
        select(Brand).where(
            Brand.id == brand_id,
            Brand.is_deleted == False
        )
    )

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    return brand


def update_brand(
    db: Session,
    brand_id: int,
    data: BrandUpdate
):
    brand = get_brand(db, brand_id)

    update_data = data.model_dump(exclude_unset=True)

    if "name" in update_data or "slug" in update_data:
        name = update_data.get("name", brand.name)
        slug = update_data.get("slug", brand.slug)

        existing_brand = db.scalar(
            select(Brand).where(
                Brand.id != brand_id,
                (Brand.name == name) | (Brand.slug == slug)
            )
        )

        if existing_brand:
            raise HTTPException(
                status_code=409,
                detail="Brand with this name or slug already exists"
            )

    for field, value in update_data.items():
        setattr(brand, field, value)

    db.commit()
    db.refresh(brand)

    return brand


def delete_brand(db: Session, brand_id: int):
    brand = get_brand(db, brand_id)

    brand.is_deleted = True

    db.commit()
from fastapi import FastAPI

from app.database import Base, engine
from app.models.brand import Brand
from app.routers import brand


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(brand.router)


@app.get("/")
def root():
    return {"message": "E-commerce Admin API"}
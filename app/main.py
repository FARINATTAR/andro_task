from fastapi import FastAPI

from app.database import Base, engine
from app.models.brand import Brand


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return {"message": "E-commerce Admin API"}
from fastapi import FastAPI, Depends  # type: ignore[reportMissingImports]
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "Product Service Running"}

@app.post("/products", response_model=schemas.ProductResponse)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
from fastapi import APIRouter, Depends, HTTPException
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductCreate, Product
from typing import Optional

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_products(product: ProductCreate,):
    repository = ProductRepository()
    service = ProductService(repository)
    return service.create_product(product)

@router.get("/product/{product_id}", response_model=Optional[dict])
def read_products(product_id: int):
    repository = ProductRepository()
    service = ProductService(repository)
    return service.get_product(product_id)

#
#@router.put("/products/{product_id}", response_model=product)
#def update_product(product_id: int, product: productCreate):
#
#@router.delete("/products/{product_id}",response_model=product)
#def delete_product(product_id: int, ):
#
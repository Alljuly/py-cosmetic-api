from fastapi import APIRouter
from app.controllers.products_controller import router as products_router

router = APIRouter()

router.include_router(products_router, prefix="/api", tags=["products"])

@router.get("/")
async def read_root():
    return{"message": "Welcome to the cosmetic API!"}
from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_product(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def get_products(self, skip: int = 0, limit=100):
        pass

    def create_product(self, product: ProductCreate):
        pass

    def update_product(self, product_id: id, product: ProductCreate):
        pass
    
    def delete_product(self, product_id: int):
        pass
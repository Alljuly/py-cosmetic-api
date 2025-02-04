from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductCreate

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository
    
    def get_product(self, product_id: int):
        return self.repository.get_product(product_id)
    
    def get_products(self, skip: int = 0, limit: int = 100):
        pass

    def create_product(self, product: ProductCreate):
        return self.repository.create_product(product)

    def update_product(self, product_id: id, product: ProductCreate):
        pass
    
    def delete_product(self, product_id: int):
        pass
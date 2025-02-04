from typing import List, Optional
from app.schemas.product_schema import ProductCreate
from app.config.database import load_csv, save_csv
import pandas as pd

class ProductRepository:
    def __init__(self):
        self.df = load_csv()

    def get_product(self, product_id: int) -> Optional[dict]:
        product = self.df[self.df["id"] == product_id]
        if not product.empty:
            return product.iloc[0].to_dict()
        return None
    

    def get_products(self, skip: int = 0, limit: int = 100) -> List[dict]:
       return None

    def create_product(self, product: ProductCreate) -> dict:
        new_id = self.df["id"].max() + 1 if not self.df.empty else 1
        new_product = {"id": new_id, **product.dict()}
        self.df = pd.concat([self.df, pd.DataFrame([new_product])], ignore_index=True)
        save_csv(self.df)
        return new_product

    def update_product(self, product_id: int, product: ProductCreate) -> Optional[dict]:
       
        return None

    def delete_product(self, product_id: int) -> Optional[dict]:
       
        return None
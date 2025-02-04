from pydantic import BaseModel

class ProductBase(BaseModel):
    name : str
    brand : str
    rate : int
    description : str
    value : float

class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config: 
        orm_mode: True
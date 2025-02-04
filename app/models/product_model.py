from sqlalchemy import Colum, Integer, String, Float
from app.config.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String)
    rate = Column(Integer)
    description = Column(String)
    value = Column(Float)
    
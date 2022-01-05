from main import Base
from sqlalchemy import Column, String, Integer


class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    protein = Column(String, nullable=False)
    carbohydrate = Column(String, nullable=False)
    fat = Column(String, nullable=False)

    def __init__(self, name, protein, carbohydrate, fat):
        self.name = name
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat



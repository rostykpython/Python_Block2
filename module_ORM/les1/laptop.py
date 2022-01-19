from sqlalchemy import Column, Integer, Date, ForeignKey
from base import Base


class Laptop(Base):
    __tablename__ = 'laptop'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    price = Column(Integer)
    screen = Column(Integer)
    added_at = Column(Date)

    def __init__(self, product, speed, ram, hd, screen, price, added_at):
        self.product = product
        self.speed = speed
        self.ram = ram
        self.hd = hd
        self.screen = screen
        self.price = price
        self.added_at = added_at

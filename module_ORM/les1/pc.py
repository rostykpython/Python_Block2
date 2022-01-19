from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class PC(Base):
    __tablename__ = 'pc'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    price = Column(Integer)
    added_at = Column(Date)
    product = relationship('product', backref='pc')

    def __init__(self, product, speed, ram, hd, price, added_at):
        self.product = product
        self.speed = speed
        self.ram = ram
        self.hd = hd
        self.price = price
        self.added_at = added_at


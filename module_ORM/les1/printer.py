from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class Printer(Base):
    __tablename__ = 'printer'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    color = Column(Boolean)
    printer_type = Column(String)
    price = Column(Integer)
    added_at = Column(Date)
    product = relationship('product', backref='printer')

    def __init__(self, product_id, color, printer_type, price, added_at):
        self.product_id = product_id
        self.color = color
        self.printer_type = printer_type
        self.price = price
        self.added_at = added_at

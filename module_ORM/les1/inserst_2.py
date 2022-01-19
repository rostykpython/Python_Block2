from datetime import date

from pc import PC
from laptop import Laptop
from printer import Printer
from prodcut import Product

from base import Session, engine, Base


Base.metadata.create_all(engine)
session = Session()

samsung_pc = Product('Samsung', 'PC')
apple_pc = Product('Apple', 'PC')
hp_pc = Product('HP', 'PC')

samsung_laptop = Product('Samsung', 'Laptop')
apple_laptop = Product('Apple', 'Laptop')
hp_laptop = Product('HP', 'Laptop')

samsung_printer = Product('Samsung', 'Printer')
apple_printer = Product('Apple', 'Printer')
hp_printer = Product('HP', 'Printer')

pc_1 = PC(samsung_pc, 2200, 16, 258, 800, date.today().isoformat())
pc_2 = PC(apple_pc, 3500, 32, 1000, 1600, date.today().isoformat())

# lp_1 = Laptop(samsung_laptop, 2200, 16, 258, 800, date.today().isoformat())
# lp_2 = Laptop(apple_laptop, 3500, 32, 1000, 1600, date.today().isoformat())

pr_1 = Printer(samsung_printer, True, 'Laser', 1200, date.today().isoformat())

session.add(pr_1)

session.commit()



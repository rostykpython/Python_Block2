from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, ARRAY, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_address_book = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/hw_address_book')
Session_address_book = sessionmaker(bind=engine_address_book)

Base = declarative_base()


class AddressBook(Base):
    __tablename__ = 'address_book'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    birthday = Column(String)
    address = Column(String)

    def __init__(self, name, phone, email, birthday, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.address = address

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Birthday: {self.birthday}'

    def __enter__(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'birthday': self.birthday,
            'address': self.address,
        }

    def __exit__(self, exception_type, exception_value, traceback):
        pass


class NoteBook(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    note = Column(String)
    tags = Column(ARRAY(String))
    added_at = Column(Date)

    def __init__(self, title, note, tags, added_at):
        self.title = title
        self.note = note
        self.tags = tags
        self.added_at = added_at

    def __str__(self):
        return f'Title: {self.title}\nNote: {self.note}\nTags: {self.tags}'

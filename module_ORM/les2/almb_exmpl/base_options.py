from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.engine import create_engine

engine = create_engine('postgresql+psycopg2://postgres:49046126w@localhost:5432/test_db')
session = sessionmaker(bind=engine)
Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    groups = relationship('Groups')

    def __init__(self, name, group_id):
        self.name = name
        self.group_id = group_id


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    students_quantity = Column(Integer)

    def __init__(self, students_quantity):
        self.students_quantity = students_quantity



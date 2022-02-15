from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text)
    email = Column(Text, nullable=False)
    login = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

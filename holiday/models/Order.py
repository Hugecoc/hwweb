from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

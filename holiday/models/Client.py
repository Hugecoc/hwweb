from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase):
    __tablename__ = 'Client'

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)

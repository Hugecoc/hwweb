from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class ClientOrder(SqlAlchemyBase):
    __tablename__ = 'client_order'

    client_id = Column(ForeignKey('Client.id'), nullable=False)
    order_id = Column(ForeignKey('Order.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    client = relationship('Client')
    order = relationship('Order')

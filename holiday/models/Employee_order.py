from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class EmployeeOrder(SqlAlchemyBase):
    __tablename__ = 'Employee_order'

    employee_id = Column(ForeignKey('Employee.id'), nullable=False)
    order_id = Column(ForeignKey('Order.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    employee = relationship('Employee')
    order = relationship('Order')

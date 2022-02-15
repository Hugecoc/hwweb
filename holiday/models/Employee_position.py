from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class EmployeePosition(SqlAlchemyBase):
    __tablename__ = 'Employee_position'

    employee_id = Column(ForeignKey('Employee.id'), nullable=False)
    posiston_id = Column(ForeignKey('Position.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    employee = relationship('Employee')
    posiston = relationship('Position')
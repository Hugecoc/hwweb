# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase

Base = SqlAlchemyBase
metadata = SqlAlchemyBase.metadata


class Client(Base):
    __tablename__ = 'Client'

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)


class Employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text)
    email = Column(Text, nullable=False)
    login = Column(Text, nullable=False)
    password = Column(Text, nullable=False)


class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class Position(Base):
    __tablename__ = 'Position'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    prescription = Column(Text, nullable=False)
    oklad = Column(Float, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class EmployeeOrder(Base):
    __tablename__ = 'Employee_order'

    employee_id = Column(ForeignKey('Employee.id'), nullable=False)
    order_id = Column(ForeignKey('Order.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    employee = relationship('Employee')
    order = relationship('Order')


class EmployeePosition(Base):
    __tablename__ = 'Employee_position'

    employee_id = Column(ForeignKey('Employee.id'), nullable=False)
    posiston_id = Column(ForeignKey('Position.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    employee = relationship('Employee')
    posiston = relationship('Position')


class ClientOrder(Base):
    __tablename__ = 'client_order'

    client_id = Column(ForeignKey('Client.id'), nullable=False)
    order_id = Column(ForeignKey('Order.id'), nullable=False)
    id = Column(Integer, primary_key=True)

    client = relationship('Client')
    order = relationship('Order')

from sqlalchemy import Column, Float, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase

metadata = SqlAlchemyBase.metadata


class Position(SqlAlchemyBase):
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
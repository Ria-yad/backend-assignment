from sqlalchemy import Column, BigInteger, Numeric, Date, String
from sqlalchemy.orm import declarative_base 

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    email = Column(String)


class Order(Base):
    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger)
    amount = Column(Numeric)
    order_date = Column(Date)


class Refund(Base):
    __tablename__ = "refunds"

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger)
    refund_amount = Column(Numeric)
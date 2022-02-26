from src.models.model import Base
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

from sqlalchemy import DateTime, Column, Numeric, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String(64))
    temperature= Column(Numeric(10, 2))
    datetime = Column(DateTime)

    def __repr__(self) :
        return f'{self.datetime} | {self.city} | {self.temperature}'

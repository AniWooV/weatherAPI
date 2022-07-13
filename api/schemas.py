from datetime import datetime
from pydantic import BaseModel


class WeatherBase(BaseModel):
    city: str
    temperature: float


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    id: int
    datetime: datetime

    class Config:
        orm_mode = True

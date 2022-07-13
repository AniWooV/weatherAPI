from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_weather_by_city(db: Session, city: str, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).filter(models.Weather.city == city).\
        order_by(models.Weather.datetime.desc()).\
        offset(skip).limit(limit).all()


def get_last_weather_by_city(db: Session, city: str):
    return db.query(models.Weather).filter(models.Weather.city == city).\
        order_by(models.Weather.datetime.desc()).first()


def get_weather_by_id(db: Session, id: int):
    return db.query(models.Weather).filter(models.Weather.id == id).first()


def get_weather(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()


def create_weather(db: Session, weather: schemas.WeatherCreate):
    dt = datetime.now()

    db_weather = models.Weather(
        city = weather.city,
        temperature = weather.temperature,
        datetime = dt
    )

    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)

    return db_weather


def delete_weather(db: Session, city: str):
    db.query(models.Weather).filter(models.Weather.city == city).delete()
    db.commit()

    return


def update_weather(db: Session, id: int, weather: schemas.WeatherCreate):
    db.query(models.Weather).\
        filter(models.Weather.id == id).\
        update({'city': weather.city, 'temperature': weather.temperature})
    db.commit()

    return

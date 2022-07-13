from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/weather/", response_model=schemas.Weather)
def create_weather(weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db=db, weather=weather)


@app.get("/weather/{id}", response_model=schemas.Weather)
def read_weather_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_weather_by_id(db, id=id)


@app.get("/weather/", response_model=list[schemas.Weather])
def read_weather(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_weather(db, skip=skip, limit=limit)


@app.get("/weather/{city}/", response_model=list[schemas.Weather])
def read_weather_by_city(city: str, db: Session = Depends(get_db)):
    weather = crud.get_weather_by_city(db, city=city)

    if weather is None:
        raise HTTPException(status_code=404, detail="City not found")

    return weather


@app.get("/weather/last/{city}/", response_model=schemas.Weather)
def read_last_weather_by_city(city: str, db: Session = Depends(get_db)):
    weather = crud.get_last_weather_by_city(db, city=city)

    if weather is None:
        raise HTTPException(status_code=404, detail="City not found")

    return weather


@app.delete("/weather/{city}/", response_model=dict)
def delete_weather(city: str, db: Session = Depends(get_db)):
    weather = crud.get_weather_by_city(db, city=city)

    if weather is None:
        raise HTTPException(status_code=404, detail="City not found")

    crud.delete_weather(db, city=city)

    return {'status': 'ok'}


@app.put("/weather/{id}/", response_model=schemas.Weather)
def update_weather(id: int, weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    if crud.get_weather_by_id(db, id=id) is None:
        raise HTTPException(status_code=404, detail="Weather not found")

    crud.update_weather(db, id=id, weather=weather)

    return  crud.get_weather_by_id(db, id=id)

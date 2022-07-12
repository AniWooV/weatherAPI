from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Weather(BaseModel):
    city: str
    temperature: float
    date: str

WEATHER_LIST = [
    {'city': 'Екатеринбург', 'temperature': 19, 'date': '18.09'},
    {'city': 'Челябинск', 'temperature': -15, 'date': '03.04'}
]

@app.get('/weather')
def get_weathers():
    return WEATHER_LIST


@app.get('/weather/{weather_id}')
def get_weather(weather_id: int):
    return WEATHER_LIST[weather_id]

@app.post('/weather/add')
def post_weather(weather: Weather):
    WEATHER_LIST.append(weather)

    return {'Status': 'Ok'}

@app.put('/weather/{weather_id}')
def put_weather(weather_id: int, weather: Weather):
    WEATHER_LIST[weather_id] = weather

    return {'Status': 'Ok'}

@app.delete('/weather/{weather_id}')
def delete_weather(weather_id: int):
    del WEATHER_LIST[weather_id]

    return {'Status': 'Ok'}

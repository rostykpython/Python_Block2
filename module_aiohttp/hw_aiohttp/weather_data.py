import asyncio
import json
import aiohttp
from weather_db.settings_of_weather_db import Session, Base, w_engine
from weather_db.models_weather_db import WeatherInfo


Base.metadata.create_all(w_engine)
session_db = Session()


CITIES = {
    'Minsk': '53.8840;27.5728',
    'Moscow': '55.7543;37.6082',
    'Kiev': '50.4364;30.5195',
}

CRAIN_INFO = {
    0: 'No rain',
    1: 'Drizzle',
    2: 'Light rain',
    3: 'Moderate rain',
    4: 'Heavy rain',
    5: 'Violent rain',
}


def check_value(input_dict: dict, value):
    for key, val in input_dict.items():
        if val == value:
            return key


async def get_weather_data(session, city):
    async with session.get(
            f'http://api.weatherapi.com/v1/current.json?key=b211bd7eb1c14e68944151354220601&q={city}&aqi=no') as response:
        weather_data = await response.json()

        db_weather_data = WeatherInfo(
            weather_data['location']['name'],
            weather_data['current']['temp_c'],
            weather_data['current']['wind_kph'],
            weather_data['current']['condition']['text'],
            weather_data['current']['condition']['icon'],
            'weather_api'
        )

        session_db.add(db_weather_data)


async def get_weather_data_grid(session, coordinates):
    async with session.get(
            f'https://gridforecast.com/api/v1/forecast/{coordinates}/202201061200?api_token=gp7z0pMbFII75x6t') as response:
        weather_text = await response.text()
        weather_data = json.loads(weather_text)

        x = weather_data['tstm']

        w_desc = {
            x > 0: 'thunderstorms unlikely',
            -4 <= x <= 0: 'thunderstorms probable',
            x <= -6: 'violent thunderstorms, tornadoes possible'
        }

        db_weather_data = WeatherInfo(
            check_value(CITIES, coordinates),
            float(weather_data['t']),
            round((weather_data['speed40'] * 3600) / 1000, 4),
            CRAIN_INFO[weather_data['crain']] + ', ' + w_desc[True],
            'No image',
            'grid_weather'
        )
        session_db.add(db_weather_data)


async def city_weather(c_dict: dict):
    tasks = []

    async with aiohttp.ClientSession() as session:
        for city, coordinates in c_dict.items():
            task1 = asyncio.create_task(get_weather_data(session, city))
            task2 = asyncio.create_task(get_weather_data_grid(session, coordinates))
            tasks.append(task1)
            tasks.append(task2)

        await asyncio.gather(*tasks)


if __name__ == '__main__':

    asyncio.run(city_weather(CITIES))
    session_db.commit()

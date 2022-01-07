import jinja2
from aiohttp import web
import aiohttp_jinja2
from weather_db.models_weather_db import WeatherInfo
from weather_db.settings_of_weather_db import Session, Base, w_engine
from sqlalchemy import desc

Base.metadata.create_all(w_engine)
session_db = Session()


async def handler(request):

    weather_data_grid = session_db.query(WeatherInfo).filter(WeatherInfo.resource == 'grid_weather').order_by(
        desc(WeatherInfo.city))
    weather_data_api = session_db.query(WeatherInfo).filter(WeatherInfo.resource == 'weather_api').order_by(
        desc(WeatherInfo.city))

    context = {
        'grid_weather': [w_info.get_info() for w_info in weather_data_grid],
        'weather_api': [w_info.get_info() for w_info in weather_data_api]
    }

    response = aiohttp_jinja2.render_template('comparing_weather.html',
                                              request,
                                              context)
    response.headers['Content-Language'] = 'en'
    return response

if __name__ == '__main__':

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(r'D:\Code_projects\Retry_python\module_aiohttp\hw1'
                                                             r'\templates'))

    app.router.add_get('/', handler, name="view")
    web.run_app(app, host="localhost")

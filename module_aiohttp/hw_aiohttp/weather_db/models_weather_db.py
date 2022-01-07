from sqlalchemy import String, Float, Column, Integer
from .settings_of_weather_db import Base


class WeatherInfo(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    temperature = Column(Float)
    wind = Column(Float)
    weather_info = Column(String)
    image = Column(String)
    resource = Column(String)

    def __init__(self, city, temperature, wind, weather_info, image, resource):
        self.city = city
        self.temperature = temperature
        self.wind = wind
        self.weather_info = weather_info
        self.image = image
        self.resource = resource

    def get_info(self):

        return [
            self.city,
            self.temperature,
            self.wind,
            self.weather_info,
            self.image,
            self.resource
        ]

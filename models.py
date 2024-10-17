import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DailyWeatherSummary(Base):
    __tablename__ = 'daily_weather_summary'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    avg_temperature = Column(Float, nullable=False)
    max_temperature = Column(Float, nullable=False)
    min_temperature = Column(Float, nullable=False)
    dominant_condition = Column(String)


def create_db():
    engine = create_engine('sqlite:///weather_data.db')
    Base.metadata.create_all(engine)

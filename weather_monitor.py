import time
from datetime import datetime
import schedule
from sqlalchemy.orm import sessionmaker
from models import DailyWeatherSummary, create_db
from utils import fetch_weather_data, process_weather_data

# Create the database
create_db()

# Database setup
from sqlalchemy import create_engine

engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)
session = Session()

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
ALERT_THRESHOLD = 35

def store_daily_summary(data):
    summary = DailyWeatherSummary(
        date=datetime.now().date(),
        location=data['location'],
        avg_temperature=data['avg_temp'],
        max_temperature=data['max_temp'],
        min_temperature=data['min_temp'],
        dominant_condition=data['condition']
    )
    session.add(summary)
    session.commit()

def check_alerts(data):
    if data['avg_temp'] > ALERT_THRESHOLD:
        print(f"Alert! The average temperature in {data['location']} is above {ALERT_THRESHOLD}°C!")

def job():
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            processed_data = process_weather_data(weather_data)
            store_daily_summary(processed_data)
            check_alerts(processed_data)

# Schedule the job every 5 minutes
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

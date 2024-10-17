from flask import Flask, render_template
from models import DailyWeatherSummary, create_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Create the database
create_db()

engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    summaries = session.query(DailyWeatherSummary).all()
    return render_template('index.html', summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)

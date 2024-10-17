Steps to run this project loacally :-

-> Clone this project or pull this using git commands

-> Install the required libraries :- in IDE terminal, run --> pip install requests sqlalchemy Flask schedule

-> Ensure latest version of python is installed locally.

-> Go to your utils.py file.

-> Replace 'your_api_key' with your actual OpenWeatherMap API key.

-> Your API key can be found under your account in "https://openweathermap.org/"

      #Run the Weather Monitoring Script
-> Right-click on weather_monitor.py in the Project view and select Run 'weather_monitor'.

-> This will start the process of fetching weather data every 5 minutes.
      
      #Run the Flask Web Application

-> Open another terminal or a new run configuration in PyCharm.

-> Right-click on app.py and select Run 'app'.

-> This will start the Flask web server.

      #Access the Web Application

-> Open your web browser.

-> Navigate to http://127.0.0.1:5000/ to see the daily weather summaries.

     #Monitor the Console

-> Check the console output of the weather_monitor.py for any alerts based on the temperature.

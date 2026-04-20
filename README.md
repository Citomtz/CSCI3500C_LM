Weather Traffic Light App 
Overview 
This project is a Python-based weather application that retrieves real-time weather data for selected cities and classifies conditions: 
Green → Good weather 
Yellow → Moderate weather  
Red → Severe weather  

The app uses the OpenWeatherMap API to fetch live weather data. 
Features 
Fetches real-time weather data 
Supports multiple cities: 
Pecos, TX 
Las Vegas, NM 
Applies traffic light logic based on: 
Temperature 
Weather conditions 
Simple and readable Python implementation 
Easy to expand into GUI or web app 

Technologies Used 
Python 3 
requests library 
OpenWeatherMap API 

Project Structure 
main.py 

Installation 
cd weather-traffic-light-app 
Install dependencies 
pip install requests 

API Setup 
Create a free account at OpenWeatherMap 
Generate an API key 
Replace the placeholder in your code: 
API_KEY = "YOURAPIKEY" 
Note: API keys may take a few minutes to activate. 

Usage 
Run the application: 
python main.py 

Example Output 
City: Pecos,TX,US 
Weather: Clear 
Temperature: 75°F 
Status: GREEN - Great weather! 
 
City: Las Vegas,NM,US 
Weather: Rain 
Temperature: 52°F 
Status: RED - Bad weather conditions! 

Author 
Lorencito Martinez

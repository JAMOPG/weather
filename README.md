# ✅ Project 
# weather
Linx Challenge


# ✅ Description of the Project
Query APIs of OpenWeather website taking temperatures of Cities around the Wolrd
Using Python as backend and framework Django.
Using ReactJs as frontend to user interface.
Data Base used was PostgreSQL.


# ✅  RoadMap
1. Click in a specific day to show your temperatures
2. Create Authentication system interface in ReactJs
3. Make more stuff be dynamic like configurations of APIs
4. Install and use at settings of Django python-decouple. 


# ✅  Requirements
1. Python 3.8
2. Django 3.2 
3. PostgreSQL


# ✅  Installation
Linux:

If virtualenv is installed properly create with:
mkvirtualenv -p python3.8

Install requirements in environment:
pip install -r requirements.txt


# ✅  Configuration
The configurations of DB need to be inputed at  "DATABASES" key inside weather/settings.py
Run: ./manage.py migrate #To create database structure but without cities in the table locations_location
Import Locations: use city.list-data.csv and import locations to locations_location table

OR:

Recommended: Create DB into your server and Restore de file "DB_to_restore.backup" with all cities of OpenWeather already in the table locations_location


# ✅  Running
./manage.py runserver
the React frontend already builded and configured inside Django Templates


# ✅  Release History
0.0.1 First Release

# ✅  Caveats
The ApiKey of OpenWeather and SecretKey of Django are Exposed because this repository will be there temporarily in public visibilization
The collections used to test APIs of Django is postman_collection.json in the root directory.(import into Postman or Insomnia)

# ✅ Contributing
https://github.com/JAMOPG/weather-linx

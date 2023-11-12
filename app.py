from flask import Flask, render_template, request
import json
from datetime import datetime
import pytz  # To handle time zones
import googlemaps  # You will need to install this package
import os  # For reading environment variables

app = Flask(__name__)

# Initialize Google Maps client with API key from environment variable
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY', 'AIzaSyBEALSB8ogqVg-lr36gYfR-cFMRxZd3btc'))

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an 'index.html' template

@app.route('/get_stations', methods=['POST'])
def get_stations():
    user_location = request.form['location']  # Assuming the user inputs their location

    try:
        with open('stations_data.json', 'r') as file:
            stations_data = json.load(file)

        if not isinstance(stations_data, list) or not all(isinstance(station, dict) for station in stations_data):
            return "Invalid data format in JSON file"

        # Filter for stations in San Francisco
        sf_stations = [station for station in stations_data if station.get('city') == 'San Francisco']

        # Add wait time and Google Maps link
        for station in sf_stations:
            station['wait_time'] = calculate_wait_time(station.get('update_time'))
            station['google_maps_link'] = get_directions_link(user_location, station.get('address'))

        return render_template('stations.html', stations=sf_stations)
    except FileNotFoundError:
        return "JSON file not found"
    except json.JSONDecodeError:
        return "Error in reading the JSON file"

def calculate_wait_time(update_time_str):
    if not update_time_str:
        return None
    try:
        update_time = datetime.fromisoformat(update_time_str)
        current_time = datetime.now(pytz.timezone('America/Los_Angeles'))  # San Francisco timezone
        wait_time = current_time - update_time
        return wait_time.seconds // 60  # Convert to minutes
    except ValueError:
        return None

def get_directions_link(user_location, station_address):
    if not user_location or not station_address:
        return None
    try:
        directions_result = gmaps.directions(user_location, station_address)
        return directions_result[0]['overview_polyline']['points']  # Simplified representation of the route
    except Exception as e:
        print(f"Error getting directions: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)

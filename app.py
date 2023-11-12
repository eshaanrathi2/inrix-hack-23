from flask import Flask, render_template, request
import json
import gmplot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an 'index.html' template

@app.route('/get_stations', methods=['POST'])
def get_stations():
    user_location = request.form['location']  # Assuming the user inputs their location

    # Read data from JSON file instead of making an API call
    try:
        with open('stations_data.json', 'r') as file:
            stations_data = json.load(file)
        
        # Process stations_data to filter based on user_location and other criteria
        # This logic depends on how you want to process the data

        return render_template('stations.html', stations=stations_data)  # Create a 'stations.html' template
    except FileNotFoundError:
        return "JSON file not found"
    except json.JSONDecodeError:
        return "Error in reading the JSON file"

if __name__ == '__main__':
    app.run(debug=True)


#creating the map
# Set the center of the map and your Google Maps API key
latitude, longitude = 37.7749, -122.4194  # San Francisco coordinates
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 12)  # 12 is the zoom level
# Add a marker
gmap.marker(latitude, longitude, title="Hello World!", color='blue')
# You can add more markers in a similar way
gmap.marker(37.7181952, -122.4729085, title="Chevron", color='green')
# Draw the map to an HTML file
gmap.draw("map.html")















'''from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual Intrix API key
API_KEY = 'your_api_key'

@app.route('/')
def index():
    return render_template('index.html')  # You'll need to create an 'index.html' template

@app.route('/get_stations', methods=['POST'])
def get_stations():
    user_location = request.form['location']  # Assuming the user inputs their location

    # API endpoint to get fuel stations data. Replace with the actual Intrix API endpoint
    url = f"https://api.intrix.com/getStations?location={user_location}&radius=5&apikey={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        stations_data = response.json()
        # Parse stations_data to extract required information
        # e.g., wait time, brand, price, CO2 emission factors
        # This depends on the structure of the response from the Intrix API

        return render_template('stations.html', stations=stations_data)  # Create a 'stations.html' template
    else:
        return "Error fetching data from the API"

if __name__ == '__main__':
    app.run(debug=True)
    '''
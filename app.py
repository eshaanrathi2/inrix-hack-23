from flask import Flask, render_template, request
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

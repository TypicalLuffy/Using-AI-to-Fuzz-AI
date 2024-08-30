import torch
import requests

# OpenWeatherMap API details
api_url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "4decbd549eecccf013bfb56244510fc2"  # Your API key

# PyTorch setup for generating random inputs
def fuzz_input():
    # Generate random latitude and longitude using PyTorch tensors
    lat = torch.randn(1).item() * 90  # Latitude ranges from -90 to 90
    lon = torch.randn(1).item() * 180  # Longitude ranges from -180 to 180
    return {"lat": lat, "lon": lon}

# Function to send fuzzed request and handle response
def fuzz_api():
    # Generate random inputs
    fuzzed_data = fuzz_input()
    
    # Prepare request with random lat/lon
    params = {
        "lat": fuzzed_data['lat'],
        "lon": fuzzed_data['lon'],
        "appid": api_key
    }
    
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            print("Valid response:", response.json())
        else:
            print(f"Unexpected status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error during API request: {e}")

# Run the fuzzing multiple times
for i in range(10):
    print(f"Fuzzing attempt {i + 1}")
    fuzz_api()

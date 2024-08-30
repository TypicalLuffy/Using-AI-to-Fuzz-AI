import torch
import requests
import json
from time import sleep

# Random input generation using PyTorch
def generate_random_input():
    return torch.randint(1, 100, (10,)).tolist()  # Generate 10 random integers between 1 and 100

# List of 10 random public APIs to fuzz
API_ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts",               # Placeholder API for testing
    "https://api.agify.io?name=michael",                        # Age prediction by name
    "https://api.genderize.io?name=michael",                    # Gender prediction by name
    "https://api.nationalize.io?name=michael",                  # Nationality prediction by name
    "https://api.coindesk.com/v1/bpi/currentprice.json",        # Bitcoin price index
    "https://dog.ceo/api/breeds/image/random",                  # Random dog image
    "https://api.exchangerate-api.com/v4/latest/USD",           # Exchange rate API
    "https://official-joke-api.appspot.com/random_joke",        # Random joke API
    "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true",  # Weather forecast
    "https://catfact.ninja/fact"                                # Random cat fact
]

# Function to send requests to APIs
def call_api(api_url, data=None):
    try:
        print(f"Calling API: {api_url}")
        if 'jsonplaceholder' in api_url:  # Handle POST for JSONPlaceholder
            response = requests.post(api_url, json={"title": "foo", "body": "bar", "userId": 1})
        else:  # GET request for other APIs
            response = requests.get(api_url)
        
        print(f"Received response from {api_url}: {response.status_code}")
        
        # Add a small delay to avoid hammering the APIs
        sleep(0.5)
        
        return response.json()  # Assuming the API returns a JSON object
    except requests.exceptions.RequestException as e:
        print(f"Error calling API {api_url}: {e}")
        return None

# Differential fuzzing comparison
def fuzz_apis():
    print("Starting fuzzing of APIs...\n")
    
    for i in range(10):  # Fuzz with 10 different random inputs
        print(f"Fuzzing round {i+1}\n---------------------")
        
        input_data = generate_random_input()
        print(f"Generated Input Data: {input_data}\n")
        
        results = {}

        for api in API_ENDPOINTS:
            result = call_api(api, input_data)
            if result:
                results[api] = result

        # Compare the results between APIs and report differences
        compare_results(results, input_data)
        print("\n")

# Compare results to identify discrepancies
def compare_results(results, input_data):
    values = list(results.values())
    
    if len(set(map(str, values))) > 1:  # Convert to string for simple comparison
        print(f"Discrepancy found for input {input_data}")
        for api, result in results.items():
            print(f"API: {api}, Result: {json.dumps(result, indent=2)}")
    else:
        print("No discrepancies found. All APIs returned similar results.")

if __name__ == "__main__":
    fuzz_apis()

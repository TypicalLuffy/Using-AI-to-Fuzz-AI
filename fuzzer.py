# fuzzer.py
import torch
import json
import requests  # Add this import statement
from time import sleep

# Function to generate random input data
def generate_random_input():
    return torch.randint(1, 100, (10,)).tolist()  # Generate 10 random integers

# Function to compare results between multiple APIs
def compare_results(results, input_data):
    values = list(results.values())
    
    if len(set(map(str, values))) > 1:  # Simple comparison by converting results to strings
        print(f"Discrepancy found for input {input_data}")
        for api, result in results.items():
            print(f"API: {api}, Result: {json.dumps(result, indent=2)}")
    else:
        print(f"No discrepancies for input {input_data}. All APIs returned similar results.")

# Function to handle calling an API
def call_api(api_url):
    try:
        print(f"Calling API: {api_url}")
        response = requests.get(api_url)  # Call the API using requests
        print(f"Received response from {api_url}: {response.status_code}")
        sleep(0.5)  # Adding a delay to avoid hammering the APIs
        return response.json()  # Assuming the API returns a JSON response
    except Exception as e:
        print(f"Error calling API {api_url}: {e}")
        return None

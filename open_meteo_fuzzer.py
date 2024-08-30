import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true"

def fuzz_open_meteo():
    input_data = generate_random_input()
    print(f"Fuzzing Open Meteo API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_open_meteo()

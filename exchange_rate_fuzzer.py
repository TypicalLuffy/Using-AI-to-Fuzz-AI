import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def fuzz_exchange_rate():
    input_data = generate_random_input()
    print(f"Fuzzing Exchange Rate API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_exchange_rate()

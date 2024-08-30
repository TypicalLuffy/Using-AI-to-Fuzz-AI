import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fuzz_coindesk():
    input_data = generate_random_input()
    print(f"Fuzzing Coindesk API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_coindesk()

import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://catfact.ninja/fact"

def fuzz_cat_fact():
    input_data = generate_random_input()
    print(f"Fuzzing Cat Fact API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_cat_fact()

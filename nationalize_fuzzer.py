import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://api.nationalize.io?name=michael"

def fuzz_nationalize():
    input_data = generate_random_input()
    print(f"Fuzzing Nationalize API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_nationalize()

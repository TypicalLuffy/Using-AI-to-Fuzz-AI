import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://dog.ceo/api/breeds/image/random"

def fuzz_dog_ceo():
    input_data = generate_random_input()
    print(f"Fuzzing Dog CEO API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_dog_ceo()

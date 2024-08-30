import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://official-joke-api.appspot.com/random_joke"

def fuzz_joke():
    input_data = generate_random_input()
    print(f"Fuzzing Joke API with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_joke()

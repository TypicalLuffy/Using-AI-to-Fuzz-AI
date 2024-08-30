import requests
from fuzzer import generate_random_input, call_api

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fuzz_jsonplaceholder():
    input_data = generate_random_input()
    print(f"Fuzzing JSONPlaceholder with input: {input_data}")
    result = call_api(API_URL)
    if result:
        print(result)

if __name__ == "__main__":
    fuzz_jsonplaceholder()

import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint, params={"key": "value"})

print(get_response.json())

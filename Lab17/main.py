import requests

api_url = "https://api.example.com/weather"

params = {
    "city":"Moscow",
    "api_key":"api_key"
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    weather = response.json()
    print(weather)
else:
    print(response.status_code)
import requests

URL = "https://opentdb.com/api.php?"
params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(URL, params=params)
response.raise_for_status()
question_data = response.json()
question_data = question_data["results"]
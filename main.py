import requests
from config import *
from datetime import datetime

base_url = "https://trackapi.nutritionix.com"
ex_url = "/v2/natural/exercise"

exercise_endpoint = f"{base_url}{ex_url}"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

query = input("Tell me which exercise you did: ")
gender = input("What is your gender ('female'/'male': ")
weight_kg = int(input("What is your weight in kg?: "))
height_cm = int(input("What is your height in cm?: "))
age = int(input("What is your age?: "))

exercise_config = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
data = response.json()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%m:%S")

exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

sheet_input = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

headers = {"Authorization": BEARER}

sheet_url = SHEET_URL

sheet_response = requests.post(sheet_url, json=sheet_input, headers=headers)
print(sheet_response.text)

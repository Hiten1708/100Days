import requests
from datetime import datetime

APP_ID = ""
APP_KEY = ""
ex_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
sp_url = "https://api.sheety.co/b9b0db9f88960288df01fbbdd6125b4e/myWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
totime = datetime.now().strftime("%H:%M:%S")
head = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

ex_input = input("What did you fucking do? ")

para = {
    "query": ex_input,
    "gender": "male",
    "weight_kg": 70.5,
    "height_cm": 170.5,
    "age": 20
}

head1 = {
    "Authorization": ""
}

response = requests.post(url=ex_ep, json=para, headers=head)
response.raise_for_status()


for char in range(len(response.json()["exercises"])):
    duration = response.json()["exercises"][char]["duration_min"]
    calories = response.json()["exercises"][char]["nf_calories"]
    exercise = response.json()["exercises"][char]["user_input"]
    ex_data = {
        "workout": {
            "date": today_date,
            "time": totime,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    send_data = requests.post(url=sp_url, json=ex_data, headers=head1)
    send_data.raise_for_status()

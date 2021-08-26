import os
API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")
GENDER = "male"
WEIGHT_KG = "105"
HEIGHT_CM = "176"
AGE = "25"
sheety_url = "https://api.sheety.co/89f436d23e73b914073612e6bcb6d739/myWorkouts/sheet1"
import requests
import datetime as dt
today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")
print(today_time)
url_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercises you did?:  ")
exercises = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url_nutritionix, json=exercises, headers=headers)
results = response.json()
print(results)
results_exercises = results.get("exercises")[0]
results_exercise_name = results_exercises.get("name")
results_exercise_duration = results_exercises.get("duration_min")
results_exercise_calories = results_exercises.get("nf_calories")

sheety_params = {
    "sheet1": {
        "date": today_date,
        "time": today_time,
        "exercise": results_exercise_name.title(),
        "duration": results_exercise_duration,
        "calories": results_exercise_calories,
    }

}
token = os.getenv("token")
bearer_header = {
    "Authorization": f"Bearer {token}"
}
response_2 = requests.post(url=sheety_url, json=sheety_params, headers=bearer_header)
response_2.raise_for_status()
print(response_2.text)


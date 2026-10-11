import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import datetime as dt


load_dotenv()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
YOUR_TWILIO_VERIFIED_NUMBER = os.getenv("MY_TWILIO_VERIFIED_NUMBER")

MY_LAT = 6.4549
MY_LONG = 3.4246

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "cnt": 4,
    }

print("⛈️  COR-Weather-Alert-Engine initialized. Querying OpenWeatherMap tracking data...")

try:
    response = requests.get(OWM_Endpoint, params=parameters, timeout=10)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False

    worst_condition_code = 900

    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < worst_condition_code:
            worst_condition_code = int(condition_code)

        if int(condition_code) < 700:
            will_rain = True

    current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if will_rain:
        print(
            f"✅ [{current_time}] Precipitation detected (Code: {worst_condition_code}). Triggering Twilio API workflow...")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella. 🌧️☔",
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{YOUR_TWILIO_VERIFIED_NUMBER}",
        )
        print(f"🚀 WhatsApp alert dispatched successfully! Status: {message.status}")
    else:
        print(
            f"☀️  [{current_time}] Log Check: Clear skies predicted (Lowest code: {worst_condition_code}). No notification required.")

except requests.RequestException as network_error:
    print(f"❌ Network Telemetry Failure: Could not reach OpenWeatherMap servers. Error: {network_error}")

except Exception as general_error:
    print(f"⚠️ Critical System Error encountered: {general_error}")



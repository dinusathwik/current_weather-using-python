import requests
import json

api_key="xxxxx"
city_name =input("enter the city name:")

url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={api_key}"

respones=requests.get(url)

data= respones.json()
logitude = data["results"][0]["geometry"]["location"]["lat"]
latitude = data["results"][0]["geometry"]["location"]["lng"]
api_key_2="xxxxxxxx"

url_2 = f"https://api.tomorrow.io/v4/weather/forecast?location={logitude},{latitude}&apikey={api_key_2}"
headers = {"accept": "application/json"}
data = requests.get(url_2, headers=headers).json()


weather_data = {"weatherCode": {
  "0": "Unknown",
  "1000": "Clear, Sunny",
  "1100": "Mostly Clear",
  "1101": "Partly Cloudy",
  "1102": "Mostly Cloudy",
  "1001": "Cloudy",
  "2000": "Fog",
  "2100": "Light Fog",
  "4000": "Drizzle",
  "4001": "Rain",
  "4200": "Light Rain",
  "4201": "Heavy Rain",
  "5000": "Snow",
  "5001": "Flurries",
  "5100": "Light Snow",
  "5101": "Heavy Snow",
  "6000": "Freezing Drizzle",
  "6001": "Freezing Rain",
  "6200": "Light Freezing Rain",
  "6201": "Heavy Freezing Rain",
  "7000": "Ice Pellets",
  "7101": "Heavy Ice Pellets",
  "7102": "Light Ice Pellets",
  "8000": "Thunderstorm"
}
}


first_entry = data['timelines']['minutely'][0]
first_time = first_entry['time']
temperature = first_entry['values']['temperature']

first_entry_hum= data['timelines']['minutely'][0]
first_time_hum = first_entry_hum['time']
humidity = first_entry_hum['values']['humidity']

first_entry_des = data['timelines']['minutely'][0]
first_time_des = first_entry_des['time']
code = first_entry_des['values']['weatherCode']


description=weather_data["weatherCode"][f"{code}"]


print(f"temperature: {temperature}")
print(f"humidity:{humidity}")
print(f"today's weather is: {description}")

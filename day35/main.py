import requests
import smtplib

api_key="034d52e5e0044a895a2b6e8f7f4be3d2"
my_email = 'patilritesh4016@gmail.com'
password = 'jjde ueoa ktuh vnww'


parameters = {
    "lat" : 18.52,
    "lon" : 73.85,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
# weather_id = data["list"][0]["weather"][0]["id"]
# print(weather_id)

for hour in data["list"]:
   condition_code = hour["weather"][0]["id"]

   if int(condition_code) < 700:
       will_rain = True

if will_rain:
    print("Bring Umbrella")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="riteshpatil401608@gmail.com",
            msg="Subject:Rain Alert\n\nHey Batman!\nTake your umbrella today.")

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

its_up = False
# Your position is within +5 or -5 degrees of the ISS position.
if iss_longitude - 5 < MY_LONG < iss_longitude + 5 and iss_latitude - 5 < MY_LAT < iss_latitude + 5:
    its_up = True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
usname = "ranarajput1409@gmail.com"
pswd = "H1t3np@tel"

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.


while True:
    time.sleep()
    if its_up and sunrise > time_now.hour > sunset:
        with smtplib.SMTP("smtp@gmail.com") as sender:
            sender.starttls()
            sender.login(user=usname, password=pswd)
            sender.sendmail(
                from_addr=usname,
                to_addrs=usname,
                msg="Subject: ISS ALERT\n\n ISS IS OVER "
            )

# BONUS: run the code every 60 seconds.


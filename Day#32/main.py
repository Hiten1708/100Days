
import datetime as dt
import pandas
import smtplib
import random
from os import listdir

files = listdir("letter_templates")
mail = ""
pswd = ""

# 1. Update the birthdays.csv

birthday_buddies = pandas.read_csv("birthdays.csv")
birth_dict = birthday_buddies.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv

for birthday in birth_dict:
    if dt.datetime.now().month == birthday['month'] and dt.datetime.now().day == birthday['day']:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
        # with the person's actual name from birthdays.csv
        with open(f"letter_templates/{random.choice(files)}") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
        to_send = birthday["email"]
        with smtplib.SMTP("smtp.gmail.com") as sender:
            sender.starttls()
            sender.login(user=mail, password=pswd)
            sender.sendmail(
                from_addr=mail,
                to_addrs=to_send,
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )

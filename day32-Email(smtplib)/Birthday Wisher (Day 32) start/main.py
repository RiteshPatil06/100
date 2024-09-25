import smtplib

my_email = 'patilritesh4016@gmail.com'
password = 'jjde ueoa ktuh vnww'




import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quotes = random.choice(all_quotes)

        print(quotes)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="riteshpatil401608@gmail.com",
                msg=f"Subject:Monday Motivation\n\n{quotes}")

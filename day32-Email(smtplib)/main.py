##################### Extra Hard Starting Project ######################
import smtplib
import datetime
import pandas
import random

my_email = 'patilritesh4016@gmail.com'
password = 'jjde ueoa ktuh vnww'


now = datetime.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthday_file = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_file.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path, 'r') as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"subject: Happy Birthday!\n\n{contents}")

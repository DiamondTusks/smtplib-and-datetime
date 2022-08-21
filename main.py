import smtplib

my_email = "diamondtuskstest@gmail.com"
password = "jkhqjiomubyvuxne"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()   # makes it secure
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="diamondtuskstest@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1980, month=1, day=1, hour=11, minute=11)
print(date_of_birth)
import datetime as dt
import pandas as pd
import random
import smtplib

my_email= "e******5@outlook.com"
password = "**********"

# obtain current day
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_tuple = (today_month,today_day)
# open csv file
df = pd.read_csv("birthdays.csv")

# create a dictionary and obtain key are month and day , value is row
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in df.iterrows()}
# if current day matches your friends name, send a mail which congratulate his/her birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict

    with open(f"letter_{random.randint(1,3)}.txt") as letter_file:
        data = letter_file.read()
        data.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp-mail.outlook.com",port=587) as st:
        st.starttls()
        st.login(user=my_email,password=password)
        st.sendmail(from_addr=my_email,
                    to_addrs=birthdays_dict["email"],
                    msg=f"Subject:HAPPY BİRTHDAY\n\n{data}")


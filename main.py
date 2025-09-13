import datetime as dt
import pandas as pd
import random
import smtplib

MY_MAIL ="msiva762003@gmail.com"
MY_PASSWORD = "libicubglrbbqoda"

today_month = (dt.datetime.now().month)
today_day = (dt.datetime.now().day)
today = (today_month, today_day)

data = pd.read_csv("birthday.csv")


birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_files:
        contents = letter_files.read()
        contents=contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_MAIL,
            to_addrs= birthday_person["email"],
            msg= f"Subject: Happy Birthday!! \n\n {contents}"
        )


import pandas
from datetime import datetime
import random
import smtplib
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

birthday_df = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()

people_to_wish = birthday_df[(birthday_df.day == now.day) & (birthday_df.month == now.month)]
row_num, col_num = people_to_wish.shape
people_to_wish.insert(col_num, "wishes", [""]*row_num)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
wishes_paths = []
for file in os.listdir("letter_templates"):
    if file.endswith(".txt"):
        wishes_paths.append(os.path.join("letter_templates", file))

for i in range(len(people_to_wish)):
    with open(random.choice(wishes_paths), "r") as file:
        wishes = file.read()
        wishes = wishes.replace("[NAME]", people_to_wish["name"][i])

    people_to_wish.loc[i, "wishes"] = wishes

# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypass"

with smtplib.SMTP("smtp.gmail.com", port=25) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    for row in people_to_wish.itertuples():
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=row[2],
                            msg=f"Subject:Happy Birthday!\n\n{row[-1]}"
                            )

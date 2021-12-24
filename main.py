from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
from datetime import date
import requests


def send_message(client, my_msg):

    client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)

base = "https://birthday-saver-api.herokuapp.com/"

res = requests.get(base + "people").json()


today = str(date.today())
curDay = today.split("-")[2]
curMonth = today.split("-")[1]


message = []

for birthdays in res:

    day = birthdays["birthday"].split("/")[1]
    month = birthdays["birthday"].split("/")[0]

    if day == curDay and month == curMonth:

        message.append(birthdays)
    

client = Client(account_sid, auth_token)


for people in message:
 
    my_msg = "Wish {0} a happy birthday!".format(people["name"])
    send_message(client, my_msg)
import requests
import json

project = input("Enter project: ")

if project == "vol":
    bot_name = "FLC-VB3sao-GreetByeThank"
else:
    bot_name = "FLC-GreetByeThank"

endpoint = "http://103.176.146.250:5043" # môi trường nlp

url = f"{endpoint}/app_codes/nlu/{bot_name}"

payload = {}
headers = {}

response = requests.request(method="GET", url=url, headers=headers, data=payload)

print(response.text)
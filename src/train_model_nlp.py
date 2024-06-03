import requests
import json

project = input("Enter project: ")

if project == "vol":
    bot_name = "FLC-VB3sao-GreetByeThank_output"
else:
    bot_name = "FLC-GreetByeThank_output"

file_path = "/home/dungca/PycharmProjects/HPC_Vaccine_VolB/data_bot/"

with open(file_path + bot_name + ".json", "r", encoding="utf-8") as f:
    data = json.load(f)

endpoint = "http://103.176.146.250:5043" # môi trường nlp

url = f"{endpoint}/train"

payload = json.dumps(data)
headers = {
  'Content-Type': 'application/json'
}

response = requests.request(method="POST", url=url, headers=headers, data=payload)

print(response.text)
import requests
import json

url = "https://datasets-server.huggingface.co/rows?dataset=gigaword&config=default&split=train&offset=0&length=100"

payload = {}
headers = {}

response = requests.request(method="GET", url=url, headers=headers, data=payload)

with open("../data/dataset.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
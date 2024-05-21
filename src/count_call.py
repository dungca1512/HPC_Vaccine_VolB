import json

id = input("Enter your ID : ")

with open(f"../data/{id}_transcript_clean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))

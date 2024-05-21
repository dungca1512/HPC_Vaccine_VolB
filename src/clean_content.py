import json

id = input("Enter ID: ")

with open(f"../data/{id}_transcript.json", "r", encoding="utf-8") as f:
    data = json.load(f)

transcript = []

for call in data:
    text = []
    for content in call["content"]:
        text.append({
            "channel": content["channel"],
            "text": content["text"]
        })
    transcript.append({
        "name": call["name"],
        "content": text
    })

with open(f"../data/{id}_transcript_clean.json", "w", encoding="utf-8") as f:
    json.dump(transcript, f, ensure_ascii=False, indent=4)

print("Done!")

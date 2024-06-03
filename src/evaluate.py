import json
import requests
import time

# project = input("Enter project: ")

start = time.time()

print("Program is running, please wait...")

with open("/home/dungca/PycharmProjects/HPC_Vaccine_VolB/data/vol_transcript_clean.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

project_info = json.load(open("/home/dungca/PycharmProjects/HPC_Vaccine_VolB/project_info/vaccine.json", encoding="utf-8"))["project_info"]

criteria_names = [i for i in project_info]

project_info_eval = {}
for criteria in criteria_names:
    project_info_eval.update({criteria: project_info[criteria]})

endpoint = "http://103.176.146.250:5005" # môi trường nlp

url = f"{endpoint}/predict/dialogue/test"

metadata = {}
response = []
agentChannel = 2

for call in data:
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        "project_info": project_info_eval,
        "transcript": call['content'],
        "metadata": metadata,
        "criteria": criteria_names,
        "fileName": call['name'],
        "agentChannel": agentChannel
    }
    payload = json.dumps(body)  
    result = requests.request(method="POST", url=url, headers=headers, data=payload).json()
    response.append(result)
    time.sleep(0.4)
    
with open('/home/dungca/PycharmProjects/HPC_Vaccine_VolB/response/vaccine_evaluate.json', 'w', encoding='utf-8') as json_file:
    json.dump(response, json_file, ensure_ascii=False, indent=4)

end = time.time()

print("Done!")

print(f"Run time: {end - start} s")


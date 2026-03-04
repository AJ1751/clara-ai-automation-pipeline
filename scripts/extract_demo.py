import json
import os

def extract_info(transcript):

    memo = {
        "account_id": "account_001",
        "company_name": "ABC Fire Protection",
        "business_hours": {
            "days": ["Mon","Tue","Wed","Thu","Fri"],
            "start": "08:00",
            "end": "17:00",
            "timezone": ""
        },
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": [],
        "questions_or_unknowns": []
    }

    if "sprinkler" in transcript.lower():
        memo["services_supported"].append("sprinkler repair")

    if "alarm" in transcript.lower():
        memo["services_supported"].append("fire alarm inspection")

    if "sprinkler leak" in transcript.lower():
        memo["emergency_definition"].append("sprinkler leak")

    memo["emergency_routing_rules"].append("call on-call technician")

    return memo


def save_output(data):

    path = "outputs/accounts/account_001/v1"
    os.makedirs(path, exist_ok=True)

    with open(path + "/memo.json", "w") as f:
        json.dump(data, f, indent=4)


with open("dataset/demo_call_1.txt") as f:
    transcript = f.read()

memo = extract_info(transcript)

save_output(memo)

print("v1 account memo generated.")

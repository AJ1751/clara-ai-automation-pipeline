import json
import os

with open("outputs/accounts/account_001/v1/memo.json") as f:
    memo = json.load(f)

agent = {
    "agent_name": "ABC Fire Assistant",
    "version": "v1",
    "voice_style": "professional",
    "system_prompt": """
You are a call assistant for ABC Fire Protection.

Business hours flow:
1 greet caller
2 ask purpose
3 collect name and phone
4 transfer call
5 fallback if transfer fails
6 close call

After hours flow:
1 greet
2 confirm emergency
3 collect name phone address
4 transfer call
"""
}

path = "outputs/accounts/account_001/v1"

with open(path + "/agent_spec.json","w") as f:
    json.dump(agent,f,indent=4)

print("agent spec generated")
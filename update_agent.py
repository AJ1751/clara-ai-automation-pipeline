import json
import os

# Load v1 memo
with open("outputs/accounts/account_001/v1/memo.json") as f:
    memo = json.load(f)

# Apply onboarding updates
memo["business_hours"]["timezone"] = "EST"
memo["emergency_routing_rules"] = ["dispatch first"]

# Create v2 folder
path = "outputs/accounts/account_001/v2"
os.makedirs(path, exist_ok=True)

# Save updated memo
with open(path + "/memo.json","w") as f:
    json.dump(memo,f,indent=4)

# Create changelog
with open(path + "/changes.md","w") as f:
    f.write("""
v1 -> v2 changes

Added timezone: EST
Emergency routing updated: dispatch first
""")

print("v2 generated successfully")
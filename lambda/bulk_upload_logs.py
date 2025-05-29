import json
import requests
import time

# Update this with your actual API Gateway endpoint URL
API_URL = "https://l7vwmrxys3.execute-api.us-east-1.amazonaws.com/prod/logs"

# Load synthetic events
with open("synthetic_vault_log_events.json", "r") as f:
    events = json.load(f)

# Send each event
for i, event in enumerate(events, start=1):
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(event)
    )

    print(f"[{i}/{len(events)}] Status: {response.status_code} | Response: {response.text}")

    # Optional delay to avoid throttling
    time.sleep(0.2)

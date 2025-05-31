import json
import requests
import time

# Replace this with your actual API endpoint
API_URL = "https://l7vwmrxys3.execute-api.us-east-1.amazonaws.com/prod/logs"

# Load synthetic logs from file
with open("vault_logs_synthetic.json", "r") as f:
    logs = json.load(f)

headers = {
    "Content-Type": "application/json"
}

success = 0
fail = 0

for log in logs:
    payload = {
        "timestamp": log["timestamp"],
        "platform": log["platform"],
        "username": log["username"],
        "action": log["action"],
        "status": log["status"]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            success += 1
        else:
            print(f"❌ Failed to send log: {response.status_code} {response.text}")
            fail += 1
    except Exception as e:
        print(f"❌ Error: {e}")
        fail += 1

    time.sleep(0.05)  # throttle to avoid overwhelming the API

print(f"✅ Upload complete: {success} success, {fail} failed")

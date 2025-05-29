import boto3
import json
from collections import defaultdict

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VaultLogEvents")

def lambda_handler(event, context):
    try:
        # Optional logging
        print("Received event:", json.dumps(event))

        response = table.scan()
        items = response.get("Items", [])

        platform_counts = defaultdict(int)
        action_counts = defaultdict(int)

        for item in items:
            platform = item.get("platform", "Unknown")
            action = item.get("action", "Unknown")

            platform_counts[platform] += 1
            action_counts[action] += 1

        result = {
            "platform_counts": dict(platform_counts),
            "action_counts": dict(action_counts)
        }

        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VaultLogEvents")

def lambda_handler(event, context):
    try:
        log = json.loads(event["body"])
        log["id"] = str(uuid.uuid4())
        log["ingested_at"] = datetime.utcnow().isoformat() + "Z"
        table.put_item(Item=log)
        return {"statusCode": 200, "body": json.dumps({"message": "Log ingested"})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

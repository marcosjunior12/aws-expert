import json
import boto3

def lambda_handler(event, context):
    table_name = 'flights'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    if "item" in event:
        item = event["item"]
        try:
            response = table.put_item(Item=item)
            return {"statusCode": 200}
        except Exception as e:
            return {"statusCode": 500, "body": str(e)}
    else:
            return {"statusCode": 400}
    
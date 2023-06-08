import json
import boto3

def lambda_handler(event, context):
    table_name = 'flights'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    try:
        response = table.scan()
        items = response["Items"]
        return {"statusCode":200, "body": items}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
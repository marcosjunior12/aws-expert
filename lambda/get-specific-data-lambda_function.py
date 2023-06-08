import boto3

def lambda_handler(event, context):
    # Configurações do DynamoDB
    table_name = 'flights'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Verifique se o evento possui o flight ID
    if "flight_id" in event:
        flight_id = event["flight_id"]
        try:
            # Obtém as informações do item específico
            response = table.get_item(Key={'id': flight_id})
            item = response['Item']
            return {"statusCode": 200, "body": item}
        except Exception as e:
            return {"statusCode": 500, "body": str(e)}
    else:
        return {"statusCode": 400, "body": "Flight ID não fornecido"}

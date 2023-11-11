import boto3
import time

def lambda_handler(event, context):
    
    t = round(time.time()) - 7200
    dynamodb = boto3.client('dynamodb')
    
    table_name = 'sample'
    column_name = 'latest_status_time'
    
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression=f'attribute_exists({column_name})'
    )
    
    # Extract the items from the response
    items = response.get('Items', [])
    
    for item in items:
        # Process the items here
        if int(item['latest_status_time']['N']) < t:
            print('yes',item)
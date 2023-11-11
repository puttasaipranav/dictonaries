import json
import os
from datetime import datetime
import time
from src.utils.aws_utils import (
    get_boto3_client,
)

import pypd



def search(event,context):
    print("Starting the search...")

    table_name = 'sample'
    column_name = 'latest_status_time'

    region = os.environ["AWS_REGION"]
    dynamodb_client = get_boto3_client(service_name="dynamodb",region= region)

    response = dynamodb_client.scan(TableName=table_name,
        FilterExpression=f'attribute_exists({column_name})'
    )

    t = round(time.time()) - 7200

    items = response.get('Items',[])

    response_data = []
    for item in items:
        if int(item['latest_status_time']['N']) < t:
            response_data.append(dict((item['sid']['S']),item['latest_status_time']['N']))

    response_str = format_response_dynamodb(response_dict=response_data)

    if(
        os.environ.get("ENVIRONMENT") not in ["dev", "local"]
        and os.environ.get("PD_ROUTING_KEY")
        and len(response_data) > 0
    ):
        send_to_pager_duty(report_name='Dynamodb delayed routes',response_data= response_str, routing_key=os.environ.get("PD_ROUTING_KEY"))



def send_to_pager_duty(report_name:str, response_data:str,routing_key:str):
    print("Sending to PagerDuty")

    pypd.EventV2.create(
        data={
            "routing_key": routing_key,
            "event_action": "trigger",
            "payload": {
                "summary": f"{report_name} - {os.environ.get('ENVRIONMENT')}",
                "timestamp": datetime.now().isoformat(),
                "source": "dynamodb",
                "severity": "info",
                "custom_details": response_data,
            },
        }
    )


def format_response_dynamodb(data:list):
    response = {data:[]}
    env = os.environ.get["ENVRIONMENT"]
    for i in data:
        i['env'] = env
        response['data'].append(i)
    return response
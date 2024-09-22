from datetime import datetime
import json
import boto3

sns_client = boto3.client('sns')
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def lambda_handler(event, context):
    # Extract the responsePayload from the event
    response_payload = (f'Hello from Lambda. Current time {current_time}')

    # Publish the message to the SNS topic
    sns_client.publish(
        TopicArn='XXXXX',
        Message=response_payload
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully')
    }

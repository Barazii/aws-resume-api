import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-north-1')

def lambda_handler(event, context):
    try:
        response = dynamodb.get_item(
            TableName= "resume",
            Key={"interviewee": {"N": "1"}}
        )
        
        # Check if the item was found
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'message ###': 'Resume not found'})
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response["Item"])
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message ###': e.response['Error']['Message']})
        }
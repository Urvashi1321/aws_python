import json
import urllib.parse
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = s3.get_object(Bucket=bucket, Key=key)
    print('File uploaded:', key)
    print(event)
    print(context)
    data = response['Body'].read().decode('utf-8')
    print(data)
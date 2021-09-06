import json
import boto3
import logging
import os

print('Loading function')
logger= logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    loggroupname=event['detail']['requestParameters']['logGroupName']
    logger.info(loggroupname)
    client = boto3.client('logs')
    response=client.put_retention_policy(
        logGroupName=loggroupname,
        retentionInDays=int(os.getenv('RetentionPeriod'))
    )
    logger.info(response)

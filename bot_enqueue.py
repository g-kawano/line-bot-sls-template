import os
import boto3
import json
import logging

sqs = boto3.client('sqs')
queue_url = os.getenv('QUEUE_URL')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Lambda Response
ok_response = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {},
    "body": ""
}
error_response = {
    "isBase64Encoded": False,
    "statusCode": 401,
    "headers": {},
    "body": ""
}


def bot_job_enqueue(sqs_client, target_queue_url, message_body):
    json_str = json.dumps(message_body)
    sqs_client.send_message(
            QueueUrl=target_queue_url,
            MessageBody=json_str
        )


def lambda_handler(event, context):
    try:
        logger.info('event: %s', event)
        bot_job_enqueue(sqs, os.getenv('QUEUE_URL'), event)

    except Exception as e:
        logger.error(e)
        return error_response

    return ok_response

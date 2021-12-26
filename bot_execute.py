import os
import json
import logging
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

channel_secret = os.getenv('LINE_CHANNEL_SECRET')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# LineBotAPI
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


def lambda_handler(event, context):
    try:
        for record in event['Records']:
            record_body = json.loads(record['body'])
            signature = record_body["headers"]["x-line-signature"]
            event_body = record_body['body']
        handler.handle(event_body, signature)
    except InvalidSignatureError as e:
        logger.error(e)
        return error_response
    except Exception as e:
        logger.error(e)
        return error_response
    return ok_response

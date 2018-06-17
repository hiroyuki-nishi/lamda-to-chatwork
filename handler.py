import json
import logging
import requests
import urllib
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

message_header = "============ Alart ===========\n"


def hello(event, context):
    logger.info("Event: " + str(event))
    __company_info(event)


def __company_info(event):
    __url = '{0}/rooms/{1}/messages'.format(os.environ['CHATWORK_URL'], os.environ['CHATWORK_ROOM_ID'])
    __payload = {'body': __parse(event)}
    __post(__url, __payload)


def __post(url, payload):
    try:
        requests.post(url, headers=__header(), params=payload)
    except:
        logger.info("Failed! Message : \n" + str(__message))
    else:
        logger.info("Success! Message posted to: \n" + str(__message))


def __header():
    return {os.environ['CHATWORK_HEADER']: os.environ['CHATWORK_API_KEY']}


def __parse(event):
    __body = json.loads(event['body'])
    logger.info(__body['webhook_event']['body'])
    return __body['webhook_event']['body']

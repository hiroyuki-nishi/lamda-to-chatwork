import json
import logging
import requests
import urllib
import os


logger = logging.getLogger()
logger.setLevel(logging.INFO)

message_header  = "============ Alart ===========\n"

def hello(event, context):
    logger.info("Event: " + str(event))
    CHATWORK_API_KEY = os.environ['CHATWORK_API_KEY']
    CHATWORK_HEADER = os.environ['CHATWORK_HEADER']
    CHATWORK_ROOM_ID = os.environ['CHATWORK_ROOM_ID']
    CHATWORK_URL = os.environ['CHATWORK_URL']
    URL = '{0}/rooms/{1}/messages'.format(CHATWORK_URL,CHATWORK_ROOM_ID)
    chatwork_message = "hoge"
    payload = {'body': chatwork_message}
    headers = {CHATWORK_HEADER: CHATWORK_API_KEY}
    try:
        requests.post(URL, headers=headers, params=payload)
    except:
        logger.info("Failed! Message : \n" + str(chatwork_message))
    else:
        logger.info("Success! Message posted to: \n" + str(chatwork_message))



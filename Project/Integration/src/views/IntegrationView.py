import logging
from flask import request, json, Response, Blueprint, g
from ..utilities import enums
from ..chat import sender as sender
from ..utilities.constants import *
import requests
from datetime import datetime


integration_api = Blueprint('integration_api', __name__)

@integration_api.route('/send', methods=['POST'])
def chat():

    data = request.get_json()
    print(json.dumps(data['message']))

    url = SPACY_PROCESS_QUESTION_ENDPOINT
    headers = {'content-type': 'application/json'}

    requestProcessQuestion = {
        "question": data['message']
    }

    response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
    question_response = json.loads(response.text)

    #print(json.dumps(data['type']))

    log_message2 ({
        "user_id": "3",
        "question": data['message'],
        "answer": question_response['answer'],
        "score": str(question_response['score']),
        "date_message": str(datetime.today())
    })
    ##if data['type'] == enums.TypeEvent.REMOVED_FROM_SPACE.value:
        ##logging.info('Rasa Bot removed from a space')

    ##else:
      ##  return format_response(data)
    return RESPONSE_MESSAGE.replace('<<QUESTION>>', question_response['question']).replace('<<RESPONSE>>', question_response['answer'])

def format_response(event):

    # Case 1: The bot was added to a room
    if event['type'] == enums.TypeEvent.ADDED_TO_SPACE.value:
        return custom_response(json.loads(WELCOME_MESSAGE), 200)
    elif event['type'] == enums.TypeEvent.CARD_CLICKED.value:
        return custom_response(json.loads(sender.send_link(event['action']['parameters'])), 200)
    else:
        return custom_response(json.loads(sender.send_message(event)), 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
def log_message2(message):

    url = ADMIN_LOGGER_ENDPOINT
    headers = {'content-type': 'application/json'}

    requestProcessQuestion =  {
        "user_id": message["user_id"],
        "question": message["question"],
        "answer": message["answer"],
        "score": message["score"],
        "date_message": message["date_message"]
    }

    requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)


@integration_api.route('/ChatSimulator', methods=['POST'])
def ChatSimulator():

    data = request.get_json()
    print(json.dumps(data['message']))

    url = SPACY_PROCESS_QUESTION_ENDPOINT
    headers = {'content-type': 'application/json'}

    requestProcessQuestion = {
        "question": data['message']
    }

    response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
    question_response = json.loads(response.text)

    log_message2 ({
        "user_id": "3",
        "question": data['message'],
        "answer": question_response['answer'],
        "score": str(question_response['score']),
        "date_message": str(datetime.today())
    })

    return RESPONSE_MESSAGE.replace('<<QUESTION>>', question_response['question']).replace('<<RESPONSE>>', question_response['answer'])

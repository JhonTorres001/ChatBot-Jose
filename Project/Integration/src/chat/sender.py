from ..utilities.constants import *
import requests
import json
from datetime import datetime


def send_message(event):

    url = SPACY_PROCESS_QUESTION_ENDPOINT
    headers = {'content-type': 'application/json'}
    requestProcessQuestion = {
        "question": event['message']['text']
    }

    print(json.dumps(requestProcessQuestion))
    response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
    question_response = json.loads(response.text)

    #loggear mensaje

    log_message({
        "user_id": event['message']['sender']['name'],
        "question": event['message']['text'],
        "answer": question_response['answer'],
        "score": str(question_response['score']),
        "date_message": str(datetime.today())
    })

    if question_response['status'] == 'FOUND':
        return RESPONSE_MESSAGE.replace('<<QUESTION>>', question_response['question']).replace('<<RESPONSE>>', question_response['answer'])
    else:
        return NOT_FOUND_MESSAGE.replace('<<QUESTION>>', event['message']['text'])


def send_link(parameters):
    url = SPACY_PROCESS_LINK_ENDPOINT
    headers = {'content-type': 'application/json'}

    title = [x for x in parameters if x['key'] == "question"][0]["value"]

    requestProcessQuestion = {
        "title": title
    }
    print(json.dumps(requestProcessQuestion))
    response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
    question_response = json.loads(response.text)

    if question_response['status'] == 'FOUND':
        return RESPONSE_MESSAGE.replace('<<QUESTION>>', question_response['title']).replace('<<RESPONSE>>', question_response['url_page'])
    else:
        return RESPONSE_MESSAGE.replace('<<QUESTION>>', 'No encontrada.').replace('<<RESPONSE>>', NOT_FOUND_LINK)


def log_message(message):

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
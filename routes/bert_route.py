from flask import Blueprint, json, request, abort
from util.db_util import connect_dynamodb, create_data_table
from controller.bert_controller import add_data, add_multiple_data
import logging
import sys
import time


bert = Blueprint('bert', __name__)

@bert.route('/pred', methods=['POST'])
def predict_text():
    init = time.time()
    try:
        if not request.is_json or 'text' not in request.get_json().keys():
            logging.error('Request is not a Json')
            fin = time.time()
            logging.info('full execution time (not JSON): '+ str(fin-init))
            abort(400)
        else:
            logging.info(sys.getsizeof(request))
            logging.info(request.get_json()['text'])
            dynamodb = connect_dynamodb()
            create_data_table(dynamodb)
            prediction = add_data(request.get_json()['text'], dynamodb)
            logging.info(prediction)
            logging.info('status code: 200')
            fin = time.time()
            logging.info('full execution time: '+ str(fin-init))
            return json.dumps(prediction)
    except Exception as e:
        fin = time.time()
        logging.info('full execution time (exception): '+ str(fin-init))
        return json.dumps(e)

@bert.route('/multiple-pred', methods=['POST'])
def predict_multiple_text():
    init = time.time()
    try:
        if not request.is_json or 'text' not in request.get_json().keys():
            logging.error('Request is not a Json')
            fin = time.time()
            logging.info('full execution time (not JSON): '+ str(fin-init))
            abort(400)
        else:
            logging.info(sys.getsizeof(request))
            logging.info(request.get_json()['text'])
            dynamodb = connect_dynamodb()
            create_data_table(dynamodb)
            prediction = add_multiple_data(request.get_json()['text'], dynamodb)
            logging.info(prediction)
            logging.info('status code: 200')
            fin = time.time()
            logging.info('full execution time: '+ str(fin-init))
            return json.dumps(prediction)
    except Exception as e:
        fin = time.time()
        logging.info('full execution time (exception): '+ str(fin-init))
        return json.dumps(e)

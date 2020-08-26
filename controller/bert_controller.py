from datetime import datetime
from models.bert_loader import BertSentimentClassifier
import logging
import time


# def add_model(model, dynamodb=None):
#     table_name = 'models'
#     existing_tables = dynamodb_client.list_tables()['TableNames']
    
#     if table_name not in existing_tables:
#         response = dynamodb.put_item(
#             TableName='models',
#             Item={
#                 'model': model,
#                 'timestamp': datetime.datetime.now().timestamp()

#             }
#         )      
#     return response
    

# def get_model(model_name, dynamodb=None):
#     table = dynamodb.Table('models')

#     try:
#         response = table.get_item(Key={'teste': nome})
#     except Exception as e:
#         print(e)
#     else:
#         if 'Item' in response:
#             return response['Item']
#         else:
#             return {'erro':'deu xabu'}

def add_data(data, dynamodb=None):
    init = time.time()
    try:
        model = BertSentimentClassifier()
        logging.info('Making prediction')
        prediction = model.predict(data)
        logging.info(f'Finished predicting... Result: {prediction}')
        response = dynamodb.put_item(
            TableName='data',
            Item={
                'data': {'S':data},
                'timestamp': {'S':str(datetime.now().timestamp())},
                'prediction': {'S':prediction},
                'ground_truth':{'S':"None"},
                'used_in_training': {'N':'0'}
            }
        )    
        response['Prediction'] = prediction
        fin = time.time()
        logging.info('Prediction time: ' + str(fin-init))
        return response
    except Exception as e:
        fin = time.time()
        logging.info('Prediction time exception: ' + str(fin-init))
        return e

def add_multiple_data(data_list, dynamodb=None):
    init = time.time()
    try:
        model = BertSentimentClassifier()
        response_list = list()
        for data in data_list:
            logging.info('Making prediction')
            prediction = model.predict(data)
            logging.info(f'Finished predicting... Result: {prediction}')
            response = dynamodb.put_item(
                TableName='data',
                Item={
                    'data': {'S':data},
                    'timestamp': {'S':str(datetime.now().timestamp())},
                    'prediction': {'S':prediction},
                    'ground_truth':{'S':"None"},
                    'used_in_training': {'N':'0'}
                }
            )    
            response['Prediction'] = prediction
            fin = time.time()
            logging.info('Prediction time: ' + str(fin-init))
            response_list.append(response)
        return response_list
    except Exception as e:
        fin = time.time()
        logging.info('Prediction time exception: ' + str(fin-init))
        return e

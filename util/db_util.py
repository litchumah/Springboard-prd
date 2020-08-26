from boto3 import client
import logging
import time


def connect_dynamodb():
    try:
        return client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    except Exception as e:
        return e


def create_data_table(dynamodb):
    init = time.time()
    try:
        table_name = 'data'
        existing_tables = dynamodb.list_tables()['TableNames']

        if table_name not in existing_tables:
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'timestamp',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'used_in_training',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'timestamp',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'used_in_training',
                        'AttributeType': 'N'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
            table.meta.client.get_waiter('table_exists').wait(TableName='data')
            logging.info('TABLE CREATED')
            fin = time.time()
            logging.info('Create table time: ' + str(fin-init))
            return dynamodb
        else:
            logging.info('TABLE ALREADY CREATED')
            fin = time.time()
            logging.info('Table already created time: ' + str(fin-init))
            return dynamodb
    except Exception as e:
        fin = time.time()
        logging.info('Create table exception time: ' + str(fin-init))
        return e
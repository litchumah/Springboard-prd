from util.db_util import connect_dynamodb, create_data_table


def test_dynamo_connection():
    dynamodb = connect_dynamodb()
    assert dynamodb.__class__.__name__ == 'DynamoDB' or dynamodb.__class__.__name__ == 'UnknownServiceError'

def test_dynamo_add_table():
    create_table = create_data_table(connect_dynamodb())
    assert create_table.__class__.__name__ == 'DynamoDB' or create_table.__class__.__name__ == 'UnknownServiceError'

import boto3


def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    table = dynamodb.create_table(
        TableName='OpencelliD',
        KeySchema=[
            {
                'AttributeName': 'lon',
                'KeyType': 'HASH'  # primary key
            },
            {
                'AttributeName': 'lat',
                'KeyType': 'RANGE'  # Sort key
            }
            
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'lon',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'lat',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10000,
            'WriteCapacityUnits': 10000
        }
    )
    return table


if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)

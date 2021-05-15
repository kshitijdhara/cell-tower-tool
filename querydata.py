import boto3
import json
from boto3.dynamodb.conditions import Key


def query_movies(lati, longi, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    table = dynamodb.Table('OpencelliD')
    print(f'Latitude: {lati} \nLongitude: {longi}')

    response = table.scan(
        #FilterExpression= Key('lon').begins_with(f'{longi}') & Key('lat').begins_with(f'{lati}') & Key('radio').eq('GSM')
        #FilterExpression= Key('lon').begins_with(f'{longi}') & Key('lat').begins_with(f'{lati}') & Key('radio').begins_with('GSM')
        FilterExpression = Key('lon').between(f'{longi[0]}', f'{longi[1]}') & Key('lat').between(f'{lati[0]}', f'{lati[1]}') & Key('radio').eq('GSM')
    )
    data = response["Items"]
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    print(json.dumps(data))


if __name__ == '__main__':
    
    print("Enter Latitude  ")
    query_lat = float(input())
    print("Enter Longitude  ")
    query_lon = float((input()))
    quer_lat = (query_lat - 0.5, query_lat + 0.5)
    quer_lon = (query_lon - 0.5, query_lon + 0.5)
    
    movies = query_movies(quer_lat, quer_lon)
    """for movie in movies:
        print(movie['cell'], ":", movie['radio'])"""

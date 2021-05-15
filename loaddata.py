from decimal import Decimal
import json
import boto3


def load_movies(movies, dynamodb=None):
    if not dynamodb:
       dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    table = dynamodb.Table('OpencelliD')
    """for data in movies:
        lat = int(data['Latitude'])
        lon = int(data['Longitude'])
        print("Adding movie:", lat, lon)
        table.put_item(Item=data)"""

    for data in movies:
        cid = int(data['cell'])
        lon = data['lon']
        lat = data['lat']
        print(f"cid = {cid}   lon = {lon}  lat = {lat}")
        #print(f'\n{data}')    
        table.put_item(Item=data)



if __name__ == '__main__':
    with open("cell tower tool\cell.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)

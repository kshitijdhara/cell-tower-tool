from decimal import Decimal
import json
import boto3
import ijson


def load_movies(data, dynamodb=None):
    if not dynamodb:
       dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    table = dynamodb.Table('OpencelliD')
    """for data in movies:
        lat = int(data['Latitude'])
        lon = int(data['Longitude'])
        print("Adding movie:", lat, lon)
        table.put_item(Item=data)"""

    cid = int(data['cell'])
    lon = data['lon']
    lat = data['lat']
    print(f"cid = {cid}   lon = {lon}  lat = {lat}")
    #print(f'\n{data}')    
    table.put_item(Item=data)



if __name__ == '__main__':
    """with open("cell tower tool\cell.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)"""
    with open("cell.json") as f:
        obj = ijson.items(f, "item")
        for o in obj:
            load_movies(o)

        
    

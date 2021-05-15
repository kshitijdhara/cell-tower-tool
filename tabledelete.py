import boto3

def delete_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

    table = dynamodb.Table('OpencelliD')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("OpencelliD table deleted.")

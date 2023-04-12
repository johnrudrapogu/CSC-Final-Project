import json
import math
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ParsingNotesDB')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    value = int(event['value'])
    bank_notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notes_count = {}
    
    for note in bank_notes:
        count = value // note
        value -= count * note
        if count > 0:
            notes_count[str(note)] = count
    
    result = {'notes_count': notes_count}
    
    response = table.put_item(
        Item={
            'ID': str(result),
            'LatestGreetingTime':now
            })
    return {
    'statusCode': 200,
    'body': json.dumps(str(result))
    }
    
    
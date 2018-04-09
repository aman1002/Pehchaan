import json
import boto3
# import demjson
from sys import argv


script, roll = argv

dynamodb = boto3.client('dynamodb')
response = dynamodb.get_item(
    TableName='present',               
    Key={'roll_number': {'S': roll}}
    )
# print(list(response['Item']['roll_number'].values())[0])

lis = list(response['Item'].values())
roll = list(lis[0].values())[0]
conf = list(lis[1].values())[0]
#print(type(roll))
#print(type(conf))
dictionary = {'roll_number':roll,
'confidence':conf}

json_string = json.dumps(dictionary)

print(json_string)

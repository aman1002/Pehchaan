from __future__ import print_function
import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    dynamo = boto3.resource('dynamodb')
    s3 = boto3.resource('s3')
    
    response = dynamodb.scan(
        TableName='present'              
        )
    table=dynamo.Table('present')

    length =len(response['Items'])

    for i in range(0,length):
	    val = response['Items'][i]['roll_number']['S']
	    table.delete_item(
	        Key={
	            'roll_number': val
	            
	        }
	        )
		    
    with open('/tmp/thumb.json', 'w') as outfile:
	    json.dump(response, outfile)
	    
    file= open('/tmp/thumb.json','rb');
    s3.Bucket('data-coll').put_object(Key='stupid/thumb.json', Body=file, ContentType='json')

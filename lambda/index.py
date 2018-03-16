from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib

print('Loading function')

dynamodb = boto3.client('dynamodb')                     #aws service clients
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')




def index_faces(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,              #refer to the event object
            "Name": key}},
            CollectionId="class_collection")
    return response
    
def update_index(tableName,faceId, personroll):
    response = dynamodb.put_item(
        TableName=tableName,
        Item={
            'RekognitionId': {'S': faceId},     #storing metadata in nosql table, in our case it is roll number of a particular face
            'roll_number': {'S': personroll}
            }
        ) 
    
# --------------- Main handler ------------------

def lambda_handler(event, context):

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']                            #event generated due to which this function is triggered 
    key = urllib.unquote_plus(
        event['Records'][0]['s3']['object']['key'].encode('utf8'))

    try:

             
        response = index_faces(bucket, key)                         #indexing of faces in the face collection
        
               
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            faceId = response['FaceRecords'][0]['Face']['FaceId']

            ret = s3.head_object(Bucket=bucket,Key=key)
            personroll = ret['Metadata']['roll_number']

            update_index('class_collection',faceId,personroll)

        # Print response to console
        print(response)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket))
        raise e

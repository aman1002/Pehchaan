import boto3
import io
from PIL import Image

rekognition = boto3.client('rekognition', region_name='us-east-1')    # service clients of AWS boto3
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    
image = Image.open("image.jpg")                           #Image method of PIL library used to convert image into bytestream
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(         #searhes the largest face in an image and compares it to already stored face collection
        CollectionId='class_collection',
        Image={'Bytes':image_binary}                                       
        )
    
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(                          #retrieval of roll number of faces that have been identified in the image
        TableName='class_collection',  
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print (face['Item']['FullName']['S'])
    else:
        print ('no match found in person lookup')

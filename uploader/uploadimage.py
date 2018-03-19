import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('1.jpg','03315603115')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('class_collection','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'roll_number':image[1]}
                    )

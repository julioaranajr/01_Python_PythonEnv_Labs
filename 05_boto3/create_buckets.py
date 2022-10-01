#Creating the Connection
import boto3

s3 = boto3.resource('s3')

#Creating a Bucket
s3.create_bucket(Bucket='ta-boto3-python-labs')

s3.create_bucket(Bucket='ta-python-labs', CreateBucketConfiguration={
    'LocationConstraint': 'eu-central-1'})

#Storing Data
s3.Object('ta-pythonlabs', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))

from urllib import response
import boto3
from datetime import date

# Let's use Amazon S3
# s3 = boto3.resource('s3')

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

client = boto3.client("s3")

response = client.list_buckets()

#print(response)
#print(response["ResponseMetadata"]["RequestId"])
#print(response["Buckets"][0]["Name"])

for bucket in response["Buckets"]:
    print(date.strftime(bucket["CreationDate"], "%H-%m-%Y %H:%M"), bucket["Name"])
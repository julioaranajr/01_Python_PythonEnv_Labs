import boto3
from datetime import datetime

client = boto3.client("s3")

response = client.list_buckets()

# print(response["Buckets"])

for bucket in response["Buckets"]:
    print(datetime.strftime(bucket["CreationDate"], "%Y-%m-%d %H:%M:%S"),
        bucket["Name"])
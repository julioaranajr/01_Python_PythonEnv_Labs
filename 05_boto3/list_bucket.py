import boto3
from datetime import datetime

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()python 

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
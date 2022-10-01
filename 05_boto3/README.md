### Install boto3
```sh
pip install boto3
```

### List Buckets example

```py
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

```


### Exercise

- Write a boto3 script that prints out all VPCs and Subnets
in your lab account.
- Then for each resource found (VPC and subnets), attach a new AWS tag "Project: Talent-Academy" where tag key is "Project" and tag value is "Talent-Academy"


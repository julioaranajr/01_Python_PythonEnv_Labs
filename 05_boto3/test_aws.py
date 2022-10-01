# Testing AWS credentials via Boto3
#!/usr/bin/env python3

import json
import boto3

client = boto3.client('sts')

response = client.get_caller_identity()

user_id = response['UserId']
account = response['Account']
arn = response['Arn']

output = {
    'UserId': user_id,
    'Account': account,
    'Arn': arn
}

print(json.dumps(output, indent=4))
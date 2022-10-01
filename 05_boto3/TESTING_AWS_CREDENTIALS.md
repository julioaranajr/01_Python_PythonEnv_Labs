# Testing AWS credentials via Boto3
```py
We can request the same information by using the Boto3 library. 
Here’s an example of a Python script (get_caller_identity.py) 
to do this:
```
```py
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
```

# Testing AWS credentials via AWS CLI
```sh
    My favorite way of testing AWS credentials is by running the following command:
    > aws sts get-caller-identity | tee
    This command will produce information about your AWS Account and User IDs:
```

'''sh
## Getting AWS Account and User IDs - Example output
```sh
    {
    "UserId": "AKIAYQV4J5VM5FWGJMGB",
    "Account": "0123456789",
    "Arn": "arn:aws:iam::0123456789:user/admin"
}
```
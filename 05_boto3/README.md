## Install boto3
To install the Boto3 library, you have to run the following command in your terminal:
```sh
pip install boto3
```
The command above will install the Boto3 library globally in your system. Alternatively, 
you can configure a Python development environment to isolate your dependencies and manage 
them separately.

## Install AWS CLI tools 
To install theAWS CLI tools, you have to run another command in your terminal:
```
pip install awscli
```
## Configuring AWS environment

AWS CLI is a set of command-line tools for accessing AWS from the terminal shell. 
Those tools are available for you through the aws command. In this section, we’ll use a 
subcommand named configure to set up an AWS environment on your laptop, workstation, or server.

To configure the AWS environment, type the following command in your terminal:

```sh

    > aws configure
 
 This command will walk you through an environment configuration process and 
 ask you for 4 things:
```

AWS Access Key: just press enter 
AWS Secret Access Key: just press and press enter 
Default region name: type -> your [aws-region-1] and enter
Default output format: type -> json and press enter

**The aws configure tool allows you not to store your AWS credentials** 
**(the AWS Access and Secret Keys) in your Python scripts.**


Note: even storing AWS Access and Secret Keys in a plain text file 
(~/.aws/credentials) is not very secure. The better and more secure 
way is to store AWS Access and Secret Keys in the encrypted store, 
for example, aws-vault.

## Testing AWS credentials
```
As soon as you’ve configured your AWS credentials, you can test that everything’s 
ready to move forward. 
```
Test your Credentials here -> [Test_AWS_Credentials.md](https://github.com/julioaranajr/01_Python_PythonEnv_Labs/blob/main/05_boto3/Test_AWS_Credentials.md)

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

### Exercises
```
- Write a boto3 script that prints out all VPCs and Subnets
in your lab account.
- Then for each resource found (VPC and subnets), attach a new AWS tag "Project: Talent-Academy" where tag key is "Project" and tag value is "Talent-Academy"
```
# Program to Loop through each existing subnets to scan for instances and add a new tag to each server
import logging
import boto3
from botocore.exceptions import ClientError
import json

session = boto3.Session(profile_name='talen-academy')
dev_s3_client = session.client('s3')


AWS_REGION = 'eu-central-1'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def get_instances_in_subnet(subnet_id):
    response = ec2_client.describe_instances(Filters=[
          {
              "Name": "subnet-id",
              "Values": [
                  subnet_id,
              ]
          },
      ])
    instance_ids = []
    for reservation in response["Reservations"]:
        instance_ids.extend([instance["InstanceId"] for instance in reservation["Instances"]])
    return instance_ids


def tag_instances(instance_ids, tag_key="MyTag", tag_value="MyTagValue"):
    ec2_client.create_tags(
        Resources=instance_ids,
        Tags=[
            {
                "Key": tag_key,
                "Value": tag_value
            },
        ])
    logger.info(f"{len(instance_ids)} instances tagged with {tag_key}:{tag_value}")


if __name__ == "__main__":
    response = ec2_client.describe_subnets()
    for subnet in response["Subnets"]:
        instance_ids = get_instances_in_subnet(subnet["SubnetId"])
        if instance_ids:
            tag_instances(instance_ids, "ScheduledLifecycle", "Yes")
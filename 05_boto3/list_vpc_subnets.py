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


def describe_vpcs(tag, tag_values, max_items):
    """
    Describes one or more of your VPCs.
    """
    try:
        # creating paginator object for describe_vpcs() method
        paginator = vpc_client.get_paginator('describe_vpcs')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        vpc_list = []

        for page in full_result['Vpcs']:
            vpc_list.append(page)

    except ClientError:
        logger.exception('Could not describe VPCs.')
        raise
    else:
        return vpc_list


if __name__ == '__main__':
    # Constants
    TAG = 'Name'
    TAG_VALUES = ['hands-on-cloud-custom-vpc']
    MAX_ITEMS = 10
    vpcs = describe_vpcs(TAG, TAG_VALUES, MAX_ITEMS)
    logger.info('VPC Details: ')
    for vpc in vpcs:
        logger.info(json.dumps(vpc, indent=4) + '\n')
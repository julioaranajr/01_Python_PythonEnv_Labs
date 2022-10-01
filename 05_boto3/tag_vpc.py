import json
import boto3

client = boto3.client('ec2')

##filters = [{'Name':'tag:Name', 'Values':['*vpc*']}]

#response = client.describe_vpcs(Filters = filters)
vpc = client.describe_vpcs()
subnets = client.describe_subnets()
print(subnets)

# print(vpcs = client.describe_vpcs(Filters = [{
#     'Name':'tag:VcpId', 'Values':['*']
# }]))
#vpcs = list(client.vpcs.filter(Filters=filters))

#vpc = vpcs["Vpcs"][0]["VpcId"]
#print(json.dumps(response, indent=4))

mytags = [{
    "Key" : "Project",
    "Value" : "Talent-Academy"
}]

# tag = client.create_tags(
#     Resources = [vpc],
#     Tags=[
#         {
#             'Key': 'string',
#             'Value': 'string'
#         },
#     ]
# )

for vpc_response in vpc['Vpcs']:
    vpcid = vpc_response.get('VpcId', [])
    client.create_tags(
    Resources = [vpcid],
    Tags=[
        {
            'Key': 'Project',
            'Value': 'Talent-Academy'
        },
    ]
)

for subnet_response in subnets['Subnets']:
    subnetid = subnet_response.get('SubnetId', [])
    client.create_tags(
    Resources = [subnetid],
    Tags=[
        {
            'Key': 'Project',
            'Value': 'Talent-Academy'
        },
    ]
)
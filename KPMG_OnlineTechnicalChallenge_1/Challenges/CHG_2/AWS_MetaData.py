# Here is an example implementation in Python using the AWS SDK (boto3) to retrieve metadata of an EC2 instance
# This code uses the boto3 library to connect to the EC2 service, 
# retrieve the metadata of the current instance and prints the data in json format.

import boto3
import json

# Connect to the EC2 service
ec2meta = boto3.client('ec2')

# Get the metadata of the current instance
instance_id = boto3.client('ec2').describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
instance_data = ec2meta.describe_instances(InstanceIds=[instance_id])

#Serialize json
json_object=json.dumps(instance_data,defauls=str,indent=4)

#Writing to Sample.json
with open("MetaOutput.json","w") as outfile:
    outfile.write(json_object)
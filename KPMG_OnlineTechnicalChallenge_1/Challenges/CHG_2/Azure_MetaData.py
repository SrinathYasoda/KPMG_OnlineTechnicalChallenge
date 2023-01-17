# For Azure SDK, you can use the azure-sdk-for-python package to interact with the Azure Management API. 
# Here's an example that retrieves the metadata for a Virtual Machine and prints it in JSON format:
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
import json

#Connect to Azure Management API
subscription_id="8bc07ae5-709d-4b62-a61e-5e90a7be9dfd"
credentials=ServicePrincipalCredentials(
    client_id="0dd5b435-634e-48a2-959e-3b0aa09494bf",
    secret="5Vw8Q~m.kv7GLy1XxBNnIgfAIMBRxY-imM~oGcof",
    tenant="a02053cb-6b82-41c7-9a29-ec09b8308c9b")

computeclient=ComputeManagementClient(credentials,subscription_id)

#Get the metadata of the current instance
vm_name="AzureVM"
resource_group_name="azure_practice_test"
vminstancedata=computeclient.virtual_machines.get(resource_group_name,vm_name)

#Format the data as JSON string
#print(json.dumps(vminstancedata.as_dict(),default=str))

with open('metaoutput.json', 'w') as f:
    json.dump(vminstancedata, f)

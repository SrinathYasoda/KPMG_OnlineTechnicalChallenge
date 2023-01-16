#### KPMG_OnlineTechnicalChallenge

Challenge #3
We have a nested object. We would like a function where you pass in the object and a key and get back the value. The choice of language and implementation is up to you.

Example Inputs object = {“a”:{“b”:{“c”:”d”}}} key = a/b/c object = {“x”:{“y”:{“z”:”a”}}} key = x/y/z value = a

Challenge 2: Azure MetaData
We need to write code that will query the meta data of an instance within AWS or Azure or GCP and provide a json formatted output. The choice of language and implementation is up to you.

Bonus Points The code allows for a particular data key to be retrieved individually Hints • Aws Documentation (https://docs.aws.amazon.com/) • Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured) • Google Documentation (https://cloud.google.com/docs)

#### Challenge:1 -- Terraform code to deploy three-tier architecture on azure

#### What is three-tier architecture?
Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: the presentation tier, or user interface; the application tier, where data is processed; and the data tier, where the data associated with the application is stored and managed.

Terraform is an open-source infrastructure as code software tool created by HashiCorp. Users define and provision data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.


#### Steps to follow:
1. One virtual network tied in three subnets.
2. Each subnet will have one virtual machine.
3. First virtual machine -> allow inbound traffic from internet only.
4. Second virtual machine -> entertain traffic from first virtual machine only and can reply the same virtual machine again.
5. App can connect to database and database can connect to app but database cannot connect to web.

_Note: Keep main and variable files different for each component_

#### Solution

#### The Terraform resources will consists of following structure

```
├── main.tf                   // The primary entrypoint for terraform resources.
├── vars.tf                   // It contain the declarations for variables.
├── output.tf                 // It contain the declarations for outputs.
├── terraform.tfvars          // The file to pass the terraform variables values.
```

#### Module

A module is a container for multiple resources that are used together. Modules can be used to create lightweight abstractions, so that you can describe your infrastructure in terms of its architecture, rather than directly in terms of physical objects.

For the solution, we have created and used five modules:
1. resourcegroup - creating resourcegroup
2. networking - creating azure virtual network and required subnets
3. securitygroup - creating network security group, setting desired security rules and associating them to subnets
4. compute - creating availability sets, network interfaces and virtual machines
5. database - creating database server and database

All the stacks are placed in the modules folder and the variable are stored under **terraform.tfvars**

To run the code you need to append the variables in the terraform.tfvars

Each module consists minimum two files: main.tf, vars.tf

resourcegroup and networking modules consists of one extra file named output.tf

#### Deployment

### Steps

**Step 0** `terraform init`

used to initialize a working directory containing Terraform configuration files

**Step 1** `terraform plan`

used to create an execution plan

**Step 2** `terraform validate`

validates the configuration files in a directory, referring only to the configuration and not accessing any remote services such as remote state, provider APIs, etc

**Step 3** `terraform apply`

used to apply the changes required to reach the desired state of the configuration


![image002](https://user-images.githubusercontent.com/48742081/212646165-51567cf9-b09a-4767-b0bf-feed74d3318d.png)


#### Challenge 2: Azure MetaData

We need to write code that will query the meta data of an instance within AWS or Azure or GCP and provide a json formatted output. 
The choice of language and implementation is up to you.

Bonus Points
The code allows for a particular data key to be retrieved individually
Hints
•         Aws Documentation (https://docs.aws.amazon.com/)
•         Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured)
•         Google Documentation (https://cloud.google.com/docs)


#### Challenge #3

We have a nested object. We would like a function where you pass in the object and a key and get back the value. 
The choice of language and implementation is up to you.

Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a



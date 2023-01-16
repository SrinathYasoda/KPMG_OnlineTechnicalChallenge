terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
    }
}

provider "azurerm"{
  features {}
  subscription_id   = "8bc07ae5-709d-4b62-a61e-5e90a7be9dfd"
  tenant_id         = "a02053cb-6b82-41c7-9a29-ec09b8308c9b"
  client_id         = "0dd5b435-634e-48a2-959e-3b0aa09494bf"
  client_secret     = "5Vw8Q~m.kv7GLy1XxBNnIgfAIMBRxY-imM~oGcof"

}

module "resourcegroup" {
  source="./modules/resourcegroup"
  name=var.name
  location=var.location
}

module "networking" {
  source         = "./modules/networking"
  location       = module.resourcegroup.location_id
  resource_group = module.resourcegroup.resource_group_name
  vnetcidr       = var.vnetcidr
  websubnetcidr  = var.websubnetcidr
  appsubnetcidr  = var.appsubnetcidr
  dbsubnetcidr   = var.dbsubnetcidr
}

module "securitygroup" {
  source="./modules/securitygroup"
  location=module.resourcegroup.location_id
  resource_group=module.resourcegroup.resource_group_name
  web_subnet_id=module.networking.websubnet_id
  app_subnet_id=module.networking.appsubnet_id
  db_subnet_id=module.networking.dbsubnet_id
}


module "compute" {
  source         = "./modules/compute"
  location = module.resourcegroup.location_id
  resource_group = module.resourcegroup.resource_group_name
  web_subnet_id = module.networking.websubnet_id
  app_subnet_id = module.networking.appsubnet_id
  web_host_name = var.web_host_name
  web_username = var.web_username
  web_os_password = var.web_os_password
  app_host_name = var.app_host_name
  app_username = var.app_username
  app_os_password = var.app_os_password
}

module "database" {
  source = "./modules/database"
  location = module.resourcegroup.location_id
  resource_group = module.resourcegroup.resource_group_name
  primary_database = var.primary_database
  primary_database_version = var.primary_database_version
  primary_database_admin = var.primary_database_admin
  primary_database_password = var.primary_database_password
}
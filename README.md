# EntraTerraformImporter
this tool helps you import existing azure resources into terraform.
>relies on the azure command line to export resources as yml and generate import commands

example terraform code included. 

## How-to

* . 
  * login in to azure with `az login`


# Gather data files

> python .\azCMDtoYAML.py   

```                      
NAME
    azCMDtoYAML.py

SYNOPSIS
    azCMDtoYAML.py COMMAND

COMMANDS
    COMMAND is one of the following:

     imports
       Generate `terraform import` commands from yaml files.

     yaml
       Create .yml output files of Azure resources
```

# terraform
full example: [usersFromYAML.tf](usersFromYAML.tf)

```hcl
locals {
  users = yamldecode(file("users.yml"))
}

resource "azuread_user" "existing" {
  for_each             = {for i, v in flatten(local.users) : v.userPrincipalName=>v}
  user_principal_name  = each.value.userPrincipalName
  display_name         = each.value.displayName
  given_name           = each.value.givenName
  surname              = each.value.surname
  preferred_language   = each.value.preferredLanguage
  usage_location       = "US"
  show_in_address_list = false
}
```
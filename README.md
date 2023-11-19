# EntraTerraformImporter
tools to aid in importing entra resources. 

## How-to

* this tool relies on the azure command line to export resources as yml. 
  * login in to azure with `az login`

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

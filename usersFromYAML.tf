terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.45.0"
    }
  }
}

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

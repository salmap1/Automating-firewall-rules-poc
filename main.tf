terraform {
  required_providers {
    paloalto = {
      source = "PaloAltoNetworks/panos"
    }
  }
}

provider "paloalto" {
  hostname = var.palo_hostname
  username = var.palo_username
  password = var.palo_password
}


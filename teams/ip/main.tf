terraform {
  required_providers {
    panos = {
      source  = "PaloAltoNetworks/panos"
      version = "~> 1.8"
    }
  }
}

provider "panos" {
  hostname = var.palo_alto_hostname
  username = var.palo_alto_username
  password = var.palo_alto_password
}

# Load and apply firewall rules from JSON files
resource "panos_security_rule" "rules" {
  for_each = jsondecode(file("${path.module}/security.json"))
  name     = each.value["name"]
  source   = each.value["source"]
  destination = each.value["destination"]
  action      = each.value["action"]
}

resource "panos_application_object" "app_rules" {
  for_each = jsondecode(file("${path.module}/application.json"))
  name     = each.value["name"]
  category = each.value["category"]
  subcategory = each.value["subcategory"]
}


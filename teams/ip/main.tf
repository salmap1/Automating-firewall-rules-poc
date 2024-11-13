provider "panos" {
  hostname     = var.PALO_ALTO_HOSTNAME
  username     = var.PALO_ALTO_USERNAME
  password     = var.PALO_ALTO_PASSWORD
}

locals {
  ip_security_rules = jsondecode(file("security_rules.json"))
}

resource "panos_security_policy" "ip_policy" {
  count                  = length(local.ip_security_rules)
  rule {
    name                  = local.ip_security_rules[count.index].name
    description           = local.ip_security_rules[count.index].description
    source_zones          = local.ip_security_rules[count.index].source_zones
    source_addresses      = local.ip_security_rules[count.index].source_addresses
    source_users          = local.ip_security_rules[count.index].source_users
    destination_zones     = local.ip_security_rules[count.index].destination_zones
    destination_addresses = local.ip_security_rules[count.index].destination_addresses
    categories            = local.ip_security_rules[count.index].categories
    applications          = local.ip_security_rules[count.index].applications
    services              = local.ip_security_rules[count.index].services
    action                = local.ip_security_rules[count.index].action
    tags                  = local.ip_security_rules[count.index].tags
  }
}


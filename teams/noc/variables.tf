variable "palo_alto_hostname" {
  type    = string
  default = ""  # Leave empty; GitHub Actions will set this as an environment variable
}

variable "palo_alto_username" {
  type    = string
  default = ""
}

variable "palo_alto_password" {
  type    = string
  default = ""
}


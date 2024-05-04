variable "region" {
  default = "ap-south-1"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "environment" {
  default = "dev"
}

variable "public_subnets_cidr" {
  default = "10.0.0.0/24"
}

variable "private_subnets_cidr" {
  default = "10.0.1.0/24"
}

variable "user_name" {
  default = "muneerahmad799"
}

variable "password" {
  default = "ABC123!#abc"
}
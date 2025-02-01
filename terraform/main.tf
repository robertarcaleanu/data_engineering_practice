terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-1"
}


locals {
  company = "robert-arc"
  environments = {
    production  = "${local.company}-data-lake-production"
    development = "${local.company}-data-lake-development"
    test = "${local.company}-my-etl-bucket"
  }
}

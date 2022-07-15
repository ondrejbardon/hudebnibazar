terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile                 = "default"
  region                  = "eu-central-1"
  shared_credentials_file = "~/.aws/personal_credentials"
}
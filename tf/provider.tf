terraform {
  backend "s3" {
    bucket = "terraformstates-cli"
    key    = "terraform/re4state.tfstate"
    region = "eu-west-2"
  }
}

provider "aws" {}

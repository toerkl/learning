provider "aws" {
  region = var.region
}

data "aws_vpc" "selected_vpc" {
  filter {
    name   = "tag:Name"
    values   = [var.vpc_name]
  }
}

data "aws_subnets" "selected_subnets" {
  filter {
    name     = "vpc-id"
    values   = [data.aws_vpc.selected_vpc.id]
  }
  filter {
    name     = "tag:aws-cdk:subnet-name"
    values   = ["PrivateSubnets"]
  }
}

data "aws_subnet" "selected_subnets" {
  for_each = toset(data.aws_subnets.selected_subnets.ids)
  id       = each.value
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  cluster_name = var.cluster_name
  cluster_version = var.cluster_version
  vpc_id = data.aws_vpc.selected_vpc.id
  subnet_ids = [for s in data.aws_subnet.selected_subnets : s.id]
  cluster_endpoint_public_access = true
  eks_managed_node_group_defaults = {
    ami_type = var.ami_type
  }
  eks_managed_node_groups = {
    main = {
      name = "node-group-1"
      instance_types = [var.instance_type]
      min_size = var.min_size
      max_size = var.max_size
      desired_size = var.desired_size
    }
  }
}
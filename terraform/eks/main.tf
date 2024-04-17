provider "aws" {
  region = var.region
}

data "aws_vpc" "selected_vpc" {
  id  = "vpc-0d215a1b36281ca41"
}

data "aws_subnets" "selected_subnets" {
  filter {
    name     = "vpc-id"
    values   = [data.aws_vpc.selected_vpc.id]
  }
  #filter {
  #  name     = var.private_subnet_tag_name
  #  values   = var.private_subnet_tag_value
  #}
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
  #subnet_ids = [for s in data.aws_subnet.selected_subnets : s.id]
  subnet_ids = ["subnet-0224cae33c5c4f85b", "subnet-0472a16a40e81a9b0", "subnet-09eb34b6899bf3e16"]
  control_plane_subnet_ids               = ["subnet-0a6064b2e08f6cdff", "subnet-0b29dfe55880bfe33", "subnet-06c7fcfb089deb594"]
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

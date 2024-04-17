variable "vpc_name" {
  description = "Name of VPC"
  type        = string
  default     = "Observability-test"
}
variable "private_subnet_tag_name" {
  description = "Tag name of private subnets"
  type        = string
  default     = "tag:aws-cdk:subnet-name"
}
variable "private_subnet_tag_value" {
  description = "Tag value of private subnets"
  type        = string
  default     = "PrivateSubnets"
}
variable "cluster_name" {
  description = "EKS cluster name"
  type        =  string
  default     =  "awesome-cluster"
}
variable "ami_type" {
  description = "AMI type for node groups"
  type        = string
  default     = "AL2023_ARM_64_STANDARD"
}
variable "instance_type" {
  description = "Instance type of worker nodes"
  type        = string
  default     = "m7g.medium"
}
variable "min_size" {
  description = "Minimum size of worker nodes"
  type        = string
  default     = "1"
}
variable "max_size" {
  description = "Maximum size of worker nodes"
  type        = string
  default     = "3"
}
variable "desired_size" {
  description = "Desired size of worker nodes"
  type        = string
  default     = "2"
}
variable "cluster_version" {
  description = "Kubernetes cluster version" 
  type        =  string
  default     =  "1.29"
}
variable "region" {
  description = "AWS region"
  default     = "eu-west-1"
  type        = string
}

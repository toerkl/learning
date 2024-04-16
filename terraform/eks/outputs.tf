output "vpc" { 
    value = data.aws_vpc.selected_vpc
}
output "subnets" { 
    value = data.aws_subnets.selected_subnets
}
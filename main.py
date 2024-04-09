#!/usr/bin/env python3

from helpers import *

# input
ip, cidr, choice, choiceNum = get_input()

# calc the new cidr, number of hosts and number of subnets in th network
newCidr, subnets, hosts = update_cidr(choice, choiceNum, cidr)

if newCidr < cidr:
    print(f"Invalid Information! original cider {cidr} is greater than the new CIDR {newCidr}")
    exit(1)

# get a list of the first and last two subnets
topSubnets, bottomSubnets = get_subnets(ip, cidr, newCidr)
# convert the subnet from CIDR to decimal presentation
subnetMask = get_subnet_in_decimal(ip, newCidr)

# results
print(f"\nIP Address: {ip}")
print(f"Subnet mask: {subnetMask}")
print(f"Subnet in CIDR: {newCidr}")
print(f"Number of hosts: {hosts}")
print(f"Number of subnets: {subnets}")

print("\nMaximum 2 subnets from top: ")
# print the Network and Broadcast Address of the first two subnets in the network 
subnets_info(topSubnets)

print("\nMaximum 2 subnets from bottom: ")
# print the Network and Broadcast Address of the last two subnets in the network 
subnets_info(bottomSubnets)
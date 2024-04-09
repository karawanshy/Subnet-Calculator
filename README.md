# Subnet Calculator

## Introduction

Subnetting is the process of dividing a larger network into smaller subnetworks, known as subnets. It is a fundamental concept in computer networking, allowing efficient allocation of IP addresses and management of network resources. 
The **Subnet Calculator** is a Python program designed to facilitate subnetting tasks by providing essential information about subnets based on user input.

## Input

* **IP Address**: Enter the IP address.
* **Subnet Mask in CIDR (Optional)**: Enter the subnet mask in CIDR notation. If not provided, the subnet will be inferred from the class of the IP address.
* **Partitioning (hosts / subnets)**: Specify whether the partitioning will be based on the number of hosts or subnets.
* **Number of Hosts/Subnets**: Enter the desired number of hosts or subnets based on the previous question.

## Output

* **Subnet Mask (Decimal Format)**: The subnet mask in decimal format.
* **Subnet in CIDR**: The subnet in CIDR notation.
* **Number of Hosts**: The total number of usable hosts.
* **Number of Subnets**: The total number of subnets.
* **For First and Last Subnets**:
    * **Network Address**: The network address of the subnet.
    * **Broadcast Address**: The broadcast address of the subnet.

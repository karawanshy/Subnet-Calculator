from math import log2, ceil
from ipaddress import IPv4Network
from validations import *

# returns the class of the given IP Address
def get_ip_class(ip):
  firstOctat = int(ip.split(".")[0])

  if firstOctat >= 0 and firstOctat <= 127:
    return 8 # class A
   
  if firstOctat >=128 and firstOctat <= 191:
    return 16 # class B
   
  if firstOctat >= 192 and firstOctat <= 223:
    return 24 # class C
   
  return 0

# calculates how much bits needed for the given number
def calc_log_of_2(num):
    return ceil(log2(int(num)))

# returns 2^num (num)
def calc_power_of_2(num):
   return 2 ** num

# updates the cider, subnet and host based on the user's partition choice
def update_cidr(choice, choiceNum, cidr):
    if choice == "subnets":
        subnet_bits = calc_log_of_2(choiceNum)
        cidr += subnet_bits
        hosts_bits = 32 - cidr
    else:
        hosts_bits = calc_log_of_2(choiceNum)
        subnet_bits = 32 - hosts_bits - cidr
        cidr = 32 - hosts_bits
        
    return cidr, calc_power_of_2(subnet_bits), calc_power_of_2(hosts_bits) - 2

# returns Network and Broacast Address of the given subnet
def get_network_broadcast_addr(subnet):
     ip, cidr = subnet.split("/")
     network = IPv4Network(f"{ip}/{str(cidr)}", strict=False)
     return str(network.network_address), str(network.broadcast_address)

# converts mask from cidr notation to decimal presentation
def get_subnet_in_decimal(ip, cidr):
   return str(IPv4Network(f"{ip}/{str(cidr)}", strict=False).netmask)

# returns the first and last subnets in the network (maximum two each) - given the ip and the cidr
def get_subnets(ip, cidr, newCidr):
  network = IPv4Network(f"{ip}/{str(cidr)}", strict=False)
  subnets = list(network.subnets(prefixlen_diff=newCidr - cidr))

  # if there is less than 4 subnets (1, 2)
  if len(subnets) < 3:
     return subnets, []
  
  return subnets[:2], subnets[-2:]

# prints the Network and Broadcast Address of the first and last subnets (maximum two each)
def subnets_info(subnetList):
   # if the list is empty - number of subnets is less than 3 so they are already printed
   if not subnetList:
      print("\nNone")
   for subnet in subnetList:
    networkAddr, broadcastAddr = get_network_broadcast_addr(str(subnet))
    print(f"\n{str(subnet)}")
    print(f"Network Address: {networkAddr}")
    print(f"Broadcast Address: {broadcastAddr}")

# gets the details from the user
def get_input():
    # get IP Address
    ip = input("Please enter an IP address: ")
    if not validate_ip(ip):
        print("Invalid IP Address!")
        exit(1)

    # get CIDR
    cidr = input("Please enter a Subnet mask in CIDR (Optional): ")
    # if cidr wasn't entered get subnet from class
    if len(cidr) == 0:
        cidr = get_ip_class(ip)
        # if not in any of the classes - A, B or C
        if cidr == 0:
           print("Invalid Class!")
    elif not validate_cidr(cidr):
        print("Invalid Subnet mask CIDR!")
        exit(1)
    cidr = int(cidr)

    # get partition - hosts or subnets
    choice = input("Please enter whether you want hosts or subnets (hosts/subnets): ")
    if not validate_choice(choice):
        print("Invalid Option!")
        exit(1)

    # get partition number based on choice - how many hosts or how many subnets
    choiceNum = input(f"Please enter number of {choice}: ")
    if not validate_number(choiceNum):
        print(f"Invalid Number of {choice}!")
        exit(1)

    return ip, cidr, choice, choiceNum

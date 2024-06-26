import re

# check if the ip address is in a legal format
def validate_ip(addr):
    pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'

    # if matches the pattern
    if re.match(pattern, addr):
        
        # check if each octat is between 0 and 255
        parts = addr.split(".")
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
        
    return False

def validate_cidr(cidr):
    if not cidr.isdigit():
        return False
    cidr = int(cidr)
    return cidr >= 0 and cidr <= 32

def validate_choice(choice):
 return choice.lower() in ["hosts", "subnets"]

def validate_number(num):
    return  num.isdigit() and int(num) > 0

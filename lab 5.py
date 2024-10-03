from itertools import filterfalse


def is_valid_part(part):
    try:
        number= int(part)
    except ValueError:
        return False
    if number< 0 or number > 255:
        return False
    if part[0] =='0' and len(part)>1:
        return False
    return True
print(is_valid_part("255"))
print(is_valid_part("256"))
print(is_valid_part("01"))
print(is_valid_part("0"))

def is_valid_ip(ip):
    parts = ip.split(',')
    if len(parts) !=4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
        return True
print(is_valid_ip("153.854.12.0"))

def decimal_to_binary(n):
    if n ==0:
        return "0"
    elif n==1:
        return '1'
    else:
        return decimal_to_binary(n//2) + str(n%2)
print(decimal_to_binary(10))

def binary_to_decimal(b):
    exp = len(b) - 1
    if exp==0:
        return int(b)
    else:
        return  binary_to_decimal(b.removeprefix(b[0])) + int(b[0]) * 2**exp


print(binary_to_decimal('101'))

def ip_to_binary(ip):
    if is_valid_ip(ip):
        return
    bin_ip=''

    for part in ip.split('.'):
        bin_ip += decimal_to_binary(int(part))+'.'

    return bin_ip.removesuffix('.')

print(ip_to_binary('125.246.54.1'))






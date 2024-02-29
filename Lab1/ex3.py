import ipaddress

#Własna implementacja walidacji ipv4

ip = input("Wprowadz IP: ")

#192.168.255.255

segments = [segment.strip() for segment in ip.split('.')]
correct_segments_sum = sum(1 for segment in segments if segment.isdigit() 
                                  and 0 <= int(segment) <= 255)

if correct_segments_sum == 4:
    print("Jest to poprawny adres ipv4\n")
else:
    print("Nie jest to poprawny adres ipv4\n")
    
#Walidacja ip korzystając z biblioteki ipaddress

def validate_ipv4(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

def validate_ipv6(address):
    try:
        ipaddress.IPv6Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

ip = input("Wprowadz IP: ")

if validate_ipv4(ip):
    print("Jest to poprawny adres IPv4.")
elif validate_ipv6(ip):
    print("Jest to poprawny adres IPv6.")
else:
    print("Nie jest to poprawny adres IPv4 ani IPv6.")




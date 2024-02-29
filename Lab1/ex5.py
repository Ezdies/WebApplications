import sys
import socket

def get_ip_by_hostname(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    
    except socket.gaierror:
        return "Nie znaleziono ip dla podanej nazwy hosta"
    
hostname = sys.argv[1]
ip = get_ip_by_hostname(hostname)
print(f'Adres IP dla hostname {hostname}, to {ip}')




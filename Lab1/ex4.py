import sys
import socket

def get_hostname_by_ip(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    
    except socket.herror:
        return "Nie znaleziono hosta dla podanego adresu ip"
    
ip = sys.argv[1]
hostname = get_hostname_by_ip(ip)
print(f'Hostname dla adresu {ip}, to {hostname}')




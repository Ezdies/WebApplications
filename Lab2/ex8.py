import socket
import sys

def scan_open_ports(address):
    try:
        ip_address = socket.gethostbyname(address)
        min_port = 1
        max_port = 65535
        for port in range(min_port, max_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            socket_open = s.connect_ex((ip_address, port))
           ## print(f"{port}")
            if socket_open == 0:
                try:
                    service_name = socket.getservbyport(port)
                    print(f"Port {port} jest otwarty - Usługa: {service_name}")
                except socket.error:
                    print(f"Port {port} jest otwarty, ale nazwa usługi jest nieznana")
            s.close()  # Zamknięcie gniazda po zakończeniu pętli
    except socket.error as e:
        print(f"Nie udało się połączyć z serwerem: {e}")

if __name__ == "__main__":
    address = sys.argv[1]

    print(f"Rozpoczynanie skanowania portów na serwerze {address}...")
    scan_open_ports(address)

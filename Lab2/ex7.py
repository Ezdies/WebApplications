import socket
import sys

def connect_to_server(address, port):
    try:
        # Sprawdź, czy podane address jest adresem IP, jeśli nie, przekonwertuj go
        try:
            ip_address = socket.gethostbyname(address)
        except socket.gaierror:
            ip_address = address
        
        # Ustanowienie połączenia TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Ustawienie limitu czasu na 5 sekund
        s.connect((ip_address, port))

        # Uzyskanie informacji o usłudze na danym porcie
        service_name = socket.getservbyport(port)
        return True, service_name
    except (socket.timeout, socket.error) as e:
        print(f"Nie udało się połączyć z serwerem: {e}")
        return False, None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python program.py <adres_hosta_lub_ip> <numer_portu>")
        sys.exit(1)

    address = sys.argv[1]
    port = int(sys.argv[2])

    print(f"Próba połączenia z serwerem {address} na porcie {port}...")
    success, service_name = connect_to_server(address, port)
    if success:
        print(f"Połączenie udane! Usługa na porcie {port}: {service_name}")
    else:
        print("Nie udało się nawiązać połączenia.")

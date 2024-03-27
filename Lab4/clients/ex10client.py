import socket


def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.encode())

    # Receive the response
    response = sock.recv(1024).decode()

    return response

def get_source(udp_datagram_hex: str):
    # Konwersja z postaci szesnastkowej na binarną
    udp_datagram_binary = bin(int(udp_datagram_hex, 16))[2:]  # Usuwamy '0b' z początku binarnego zapisu
    source_port_binary = udp_datagram_binary[:16]
    return int(source_port_binary, 2)

def get_destination(udp_datagram_hex: str):
    # Konwersja z postaci szesnastkowej na binarną
    udp_datagram_binary = bin(int(udp_datagram_hex, 16))[2:]  # Usuwamy '0b' z początku binarnego zapisu
    destination_port_binary = udp_datagram_binary[16:32]
    return int(destination_port_binary, 2)

def get_data(udp_datagram_hex: str):
    # Konwersja z postaci szesnastkowej na binarną
    udp_datagram_binary = bin(int(udp_datagram_hex, 16))[2:]  # Usuwamy '0b' z początku binarnego zapisu
    
    # Wyodrębnienie pól danych
    data_binary = udp_datagram_binary[-64:]  # Ignorujemy 64 pierwsze bity, które reprezentują nagłówek UDP
    
    # Dzielimy binarny ciąg na 8-bitowe bloki, a następnie przekształcamy każdy blok na liczbę całkowitą i dalej na znak ASCII
    data_chunks = [int(data_binary[i:i+8], 2) for i in range(0, len(data_binary), 8)]
    data_string = ''.join(chr(chunk) for chunk in data_chunks)
    
    return data_string

def concat_all(udp_datagram_hex: str):
    return f"zad14odp;src;{get_source(udp_datagram_hex)};dst;{get_destination(udp_datagram_hex)};data;{get_data(udp_datagram_hex)}"



if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv4.settimeout(1)  # Increase timeout to 5 seconds
    server_address = ('0.0.0.0', 2900)
    
    # Pełny zapis datagramu UDP w postaci szesnastkowej
    udp_datagram_hex = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"

    message_to_send = concat_all(udp_datagram_hex)
    try:
        sockIPv4.connect(server_address)
        response = send_receive_message(sockIPv4, message_to_send)
        print("Received response:", response)
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()
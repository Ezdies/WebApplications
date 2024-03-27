import socket


def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.encode())

    # Receive the response
    response = sock.recv(1024).decode()

    return response

def get_version(tcpip_datagram_hex: str):
    hex_pairs = [tcpip_datagram_hex[i:i+2] for i in range(0, len(tcpip_datagram_hex), 2)]
    binary_representation = ''.join([bin(int(pair, 16))[2:].zfill(8) for pair in hex_pairs])
    version_number_binary = binary_representation[0:4]
    return int(version_number_binary, 2)

def get_source_ip(tcpip_datagram_hex: str):
    # Konwersja datagramu TCP/IP na postać binarną
    tcpip_datagram_binary = bin(int(tcpip_datagram_hex, 16))[2:]
    
    # Pobranie adresu IP źródłowego z nagłówka IPv4
    source_ip_binary = tcpip_datagram_binary[96:128]  # Od 12. do 15. bajtu nagłówka
    source_ip_hex = hex(int(source_ip_binary, 2))[2:]  # Konwersja na szesnastkowy
    
    # Formatowanie adresu IP źródłowego w postaci standardowej
    formatted_source_ip = '.'.join([str(int(source_ip_hex[i:i+2], 16)) for i in range(0, len(source_ip_hex), 2)])
    
    return formatted_source_ip

def get_destination_ip(tcpip_datagram_hex: str):
    # Konwersja datagramu TCP/IP na postać binarną
    tcpip_datagram_binary = bin(int(tcpip_datagram_hex, 16))[2:]
    
    # Pobranie adresu IP źródłowego z nagłówka IPv4
    source_ip_binary = tcpip_datagram_binary[128:160]  # Od 12. do 15. bajtu nagłówka
    source_ip_hex = hex(int(source_ip_binary, 2))[2:]  # Konwersja na szesnastkowy
    
    # Formatowanie adresu IP źródłowego w postaci standardowej
    formatted_source_ip = '.'.join([str(int(source_ip_hex[i:i+2], 16)) for i in range(0, len(source_ip_hex), 2)])
    
    return formatted_source_ip

def get_protocol_type(tcpip_datagram_hex: str):
    hex_pairs = [tcpip_datagram_hex[i:i+2] for i in range(0, len(tcpip_datagram_hex), 2)]
    binary_representation = ''.join([bin(int(pair, 16))[2:].zfill(8) for pair in hex_pairs])
    protocol_type_binary = binary_representation[72:80]
    return int(protocol_type_binary, 2)
    

def concat_all(tcpip_datagram_hex: str):
    return f"zad15odpA;ver;{get_version(tcpip_datagram_hex)};srcip;{get_source_ip(tcpip_datagram_hex)};dstip;{get_destination_ip(tcpip_datagram_hex)};type;{get_protocol_type(tcpip_datagram_hex)}"



if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv4.settimeout(1)  # Increase timeout to 5 seconds
    server_address = ('127.0.0.1', 2911)
    
    # Pełny zapis datagramu UDP w postaci szesnastkowej
    tcpip_datagram_hex = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"

    message_to_send = concat_all(tcpip_datagram_hex)
    try:
        sockIPv4.connect(server_address)
        response = send_receive_message(sockIPv4, message_to_send)
        print("Received response:", response)
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()
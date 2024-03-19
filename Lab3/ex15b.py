import socket


def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.encode())

    # Receive the response
    response = sock.recv(1024).decode()

    return response

def concat_all(tcpip_datagram_hex: str):
    return f"zad15odpB;srcport;{get_source_port(tcpip_datagram_hex)};dstport;{get_destination_port(tcpip_datagram_hex)};data;{get_tcp_data(tcpip_datagram_hex)}"


###tcp stuff

def get_source_port(tcpip_datagram_hex: str):
    hex_pairs = [tcpip_datagram_hex[i:i+2] for i in range(0, len(tcpip_datagram_hex), 2)]
    binary_representation = ''.join([bin(int(pair, 16))[2:].zfill(8) for pair in hex_pairs])
    version_number_binary = binary_representation[160:176]
    return int(version_number_binary, 2)

def get_destination_port(tcpip_datagram_hex: str):
    hex_pairs = [tcpip_datagram_hex[i:i+2] for i in range(0, len(tcpip_datagram_hex), 2)]
    binary_representation = ''.join([bin(int(pair, 16))[2:].zfill(8) for pair in hex_pairs])
    version_number_binary = binary_representation[176:192]
    return int(version_number_binary, 2)

def get_tcp_data(tcpip_datagram_hex: str):
    tcpip_datagram_binary = bin(int(tcpip_datagram_hex, 16))[2:]  # Usuwamy '0b' z początku binarnego zapisu
    data_binary = tcpip_datagram_binary[-208:]  # Ignorujemy 64 pierwsze bity, które reprezentują nagłówek UDP
    data_chunks = [int(data_binary[i:i+8], 2) for i in range(0, len(data_binary), 8)]
    data_string = ''.join(chr(chunk) for chunk in data_chunks)
    return data_string

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







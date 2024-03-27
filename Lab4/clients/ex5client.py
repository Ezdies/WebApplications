import socket

def send_receive_message(sock, server_address, message):
    # Send the message to the server
    sock.sendto(message.encode('utf-8'), server_address)

    try:
        # Receive the response
        response, _ = sock.recvfrom(1024)
        return response.decode()
    except socket.timeout:
        return "Timeout occurred while waiting for response from the server."

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv4.settimeout(5)  # Increase timeout to 5 seconds
    server_address = ('127.0.0.1', 2906)

    # Get the local IP address
    local_ip = socket.gethostbyname(socket.gethostname())

    # Send the local IP address to the server
    response = send_receive_message(sockIPv4, server_address, local_ip)
    
    print("Received hostname:", response)
    
    sockIPv4.close()
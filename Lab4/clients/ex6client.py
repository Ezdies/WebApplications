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
    server_address = ('127.0.0.1', 2907)

    # Get the hostname
    hostname = socket.gethostname()

    # Send the hostname to the server
    response = send_receive_message(sockIPv4, server_address, hostname)

    print("Received IP address:", response)

    sockIPv4.close()
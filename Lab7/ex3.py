import socket
import select

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
    UDP_PORTS = [34666, 17666, 53666]
    TCP_PORT = 2913  # Example TCP port to receive information about
    
    udp_sockets = []
    responses = {}
    tcp_response = ""

    # Create sockets for each UDP port
    for port in UDP_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)  # Increase timeout to 1 second
        server_address = ('127.0.0.1', port)
        udp_sockets.append((sock, server_address))

    # Send a message to each server for UDP port knocking
    message_to_send = "PING"
    for sock, server_address in udp_sockets:
        response = send_receive_message(sock, server_address, message_to_send)
        responses[server_address] = response

    # Print UDP responses
    for addr, response in responses.items():
        print(f"Received response from {addr}: {response}")

    # Create TCP socket for receiving information
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(5)  # Increase timeout to 1 second

    try:
        # Connect to the server's TCP port
        tcp_socket.connect(('127.0.0.1', TCP_PORT))
        # Receive the TCP response
        tcp_response = tcp_socket.recv(1024).decode()
    except socket.timeout:
        tcp_response = "Timeout occurred while waiting for TCP response."
    finally:
        tcp_socket.close()

    # Print TCP response
    print(f"Received TCP response: {tcp_response}")

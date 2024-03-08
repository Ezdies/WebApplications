import socket

def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.encode('utf-8'))

    # Receive the response with a timeout
    try:
        response = sock.recv(1024).decode()
        return response
    except socket.timeout:
        print("Timeout occurred while waiting for response from the server.")
        return None

if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)  # Set timeout to 5 seconds
    result = sockIPv4.connect_ex(('0.0.0.0', 2900))
    
    if result == 0:
        print('Connected')
        while True:
            # Send a message to the server
            message_to_send = input("Enter message to send (type 'exit' to quit): ")
            if message_to_send.lower() == 'exit':
                break
            response = send_receive_message(sockIPv4, message_to_send)
            if response is not None:
                print("Received response:", response)
    else:
        print("Failed to connect")
        
    sockIPv4.close()

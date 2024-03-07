import socket

def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.encode('utf-8'))

    # Receive the response
    response = sock.recv(1024).decode()

    return response

if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(1)
    result = sockIPv4.connect_ex(('212.182.24.236', 22))
    
    if result == 0:
        print('Connected')
        # Send a message to the server
        message_to_send = "Hello, server!"
        response = send_receive_message(sockIPv4, message_to_send)
        
        print("Received response:", response)
    else:
        print("Failed to connect")
        
    sockIPv4.close()

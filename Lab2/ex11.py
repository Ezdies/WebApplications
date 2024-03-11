import socket

def send_receive_message(sock, message):
    # Uzupełnienie wiadomości do 20 znaków, jeśli jest za krótka
    message_padded = message.ljust(20)

    # Przycięcie wiadomości do 20 znaków, jeśli jest za długa
    message_truncated = message[:20]

    # Send the message to the server
    sock.sendall(message_padded.encode('utf-8'))

    # Receive the response
    response = sock.recv(1024).decode()

    return response

if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(1)
    
    try:
        server_address = ('0.0.0.0', 2908)
        sockIPv4.connect(server_address)
        print('Connected')
        
        # Send a message to the server
        message_to_send = input("Enter message to send (max 20 characters): ")

        response = send_receive_message(sockIPv4, message_to_send)
        
        print("Received response:", response)
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

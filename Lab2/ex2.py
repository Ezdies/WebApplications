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
    
    try:
        sockIPv4.connect(('0.0.0.0', 2900))
        print('Connected')
        
        # Send a message to the server
        message_to_send = "Hello, server!"
        response = send_receive_message(sockIPv4, message_to_send)
        
        print("Received response:", response)
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

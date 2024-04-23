import socket

def send_receive_message(sock, message):
    # Send the message to the server
    sock.sendall(message.to_bytes(4, byteorder='big'))

    # Receive the response
    response = sock.recv(1024).decode()

    return response

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(1)
    
    try:
        sockIPv4.connect(('127.0.0.1', 2912))
        print('Connected')
        
        while True:
            # Send a message to the server
            liczba = int(input("Podaj liczbe do wylosowania: "))
            response = send_receive_message(sockIPv4, liczba)
            print("Received response:", response)
            if response.startswith("You won"):
                break
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

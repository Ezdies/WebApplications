import socket

def send_receive_message(sock, message, host):
    try:
        # Create HTTP request with the message and User-Agent header
        http_request = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n\r\n{message}"
        
        # Send the HTTP request to the server
        sock.sendall(http_request.encode('utf-8'))

        # Receive the response
        response = sock.recv(1024).decode()

        return response
    except socket.timeout:
        print("Timeout occurred while sending/receiving data.")
        return None

if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)  # Set timeout to 5 seconds
    host = 'httpbin.org'  # Corrected the hostname
    port = 80
    
    try:
        addresses = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
        family, socktype, proto, canonname, sockaddr = addresses[0]  # Select the first address

        sockIPv4.connect(sockaddr)
        print('Connected')
        
        # Send a message to the server
        message_to_send = "Hello, server!"
        response = send_receive_message(sockIPv4, message_to_send, host)
        
        if response is not None:
            print("Received response:", response)
            with open('server_response.txt', 'w') as file:
                file.write(response)
                print("Response saved to server_response.txt")
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

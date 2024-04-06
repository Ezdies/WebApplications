import socket

def send_receive_message(sock, message, host):
    try:
        # Create HTTP request with the message and User-Agent header
        http_request = f"GET /image/png HTTP/1.1\r\nHost: {host}\r\n\r\n{message}"
        
        # Send the HTTP request to the server
        sock.sendall(http_request.encode('utf-8'))

        # Receive the response
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

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
        
        if b"Content-Type: image/png" in response:
            # Find the start of the image data
            start_index = response.find(b'\r\n\r\n') + 4
            image_data = response[start_index:]
            
            # Save image data to a file
            with open('image.png', 'wb') as file:
                file.write(image_data)
                print("Image saved to image.png")
        else:
            print("No image found in the response.")
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

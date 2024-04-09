import socket

def send_receive_message(sock, message):
    try:
        sock.sendall(message.encode('utf-8'))

        response = sock.recv(4096).decode()

        return response
    except socket.timeout:
        print("Timeout occurred while sending/receiving data.")
        return None

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)
    host = 'httpbin.org'
    port = 80
    
    try:
        addresses = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
        family, socktype, proto, canonname, sockaddr = addresses[0]

        sockIPv4.connect(sockaddr)
        print('Connected')
        
        http_request = "GET /forms/post HTTP/1.1\r\nHost: httpbin.org\r\n\r\n"
        response = send_receive_message(sockIPv4, http_request)
        
        print(response)
        
        form_data = {}
        form_data['custname'] = input("Enter customer name: ")
        form_data['custtel'] = input("Enter telephone: ")
        form_data['custemail'] = input("Enter email address: ")
        form_data['size'] = input("Enter pizza size (small/medium/large): ")
        form_data['topping'] = input("Enter pizza toppings (comma separated): ").split(',')
        form_data['delivery'] = input("Enter preferred delivery time (HH:MM): ")
        form_data['comments'] = input("Enter delivery instructions: ")

        encoded_form_data = "&".join([f"{key}={value}" for key, value in form_data.items()])
        http_request = f"""POST /post HTTP/1.1\r\nHost: httpbin.org\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(encoded_form_data)}\r\n\r\n{encoded_form_data}"""

        response = send_receive_message(sockIPv4, http_request)
        
        if response is not None:
            print("Received response:")
            print(response)
        
    except socket.error as e:
        print(f"Failed to connect: {e}")
    finally:
        sockIPv4.close()

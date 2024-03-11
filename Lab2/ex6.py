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

if __name__== '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv4.settimeout(5)  # Increase timeout to 5 seconds
    server_address = ('127.0.0.1', 2901)  # Server address and port
    
    print("Connected")
    
    while True:
        # Get user input for the message (number, operator, number)
        print("If either of inputs is 'exit', quit.")
        num1 = input("Enter the first number: ")
        if num1.lower() == 'exit':
            break
            
        operator = input("Enter the operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            break
            
        num2 = input("Enter the second number: ")
        if num2.lower() == 'exit':
            break

        # Construct the message
        message_to_send = f"{num1} {operator} {num2}"

        # Send message to the server
        response = send_receive_message(sockIPv4, server_address, message_to_send)
        if response is not None:
            print("Received response:", response)

    sockIPv4.close()

import socket

def connect_to_server(ip, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        print("Connected to server.")
        return client_socket
    except socket.error as e:
        print(f"Connection error: {e}")
        return None

def send_message(client_socket, message):
    try:
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    except socket.error as e:
        print(f"Error sending message: {e}")

def close_connection(client_socket):
    try:
        if client_socket:
            client_socket.close()
            print("Connection closed.")
    except socket.error as e:
        print(f"Error closing connection: {e}")

def run_client():
    client_socket = connect_to_server('127.0.0.1', 6666)
    if client_socket:
        try:
            while True:
                message = input("Enter message (press Enter to exit): ")
                if not message:
                    break
                send_message(client_socket, message)

        finally:
            close_connection(client_socket)

if __name__ == '__main__':
    run_client()

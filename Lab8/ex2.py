import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        print(f"Client connected: {self.address}")

        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            print(f"Received from {self.address}: {data.decode()}")
            self.connection.sendall(data)

        print(f"Client disconnected: {self.address}")
        self.connection.close()

class EchoServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = None

    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(5)
            print(f"Echo server started on {self.ip}:{self.port}")

            while True:
                connection, address = self.server_socket.accept()
                client_thread = ClientThread(connection, address)
                client_thread.start()

        except socket.error as e:
            print(f"Error: {e}")

        finally:
            if self.server_socket:
                self.server_socket.close()

if __name__ == '__main__':
    echo_server = EchoServer('127.0.0.1', 6666)
    echo_server.start()

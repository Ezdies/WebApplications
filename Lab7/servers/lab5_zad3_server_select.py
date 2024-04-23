import socket
import select
import time
from time import gmtime, strftime

HOST = '127.0.0.1'
TCP_PORT = 2913
UDP_PORTS = [34666, 17666, 53666]


def gettime():
    return str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


def set_up_udp_ports(host, ports):
    udpsockets = []
    for port in ports:
        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpsock.bind((host, port))
        udpsockets.append(udpsock)
    return udpsockets


def open_tcp_port(host, port):
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        tcpsock.bind((host, port))
        tcpsock.listen(1)
        conn, addr = tcpsock.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('[%s] Server got %s at TCP: %s' % (gettime(), data, port))
            conn.send("Congratulations! You found the hidden".encode())
        conn.close()
        print("[%s] Port knocking successful ... " % gettime())
    except Exception as e:
        print(f"Error occurred while opening TCP port: {e}")
    finally:
        tcpsock.close()


def clients_are_the_same(clients_list):
    
    return clients_list[0][0] == clients_list[1][0] == clients_list[2][0]


def run(host, tcpport):
    udpsockets = set_up_udp_ports(HOST, UDP_PORTS)
    i = 0
    clients_list = []

    for udpsock in udpsockets:
        try:
            ready = select.select([udpsock], [], [], 5)
            if ready[0]:
                data, client = udpsock.recvfrom(100)
                print(f"{data} , {client}")
                if not data:
                    break
                if data.decode() == 'PING':
                    print('[%s] Server got PING ... ' % gettime())
                    udpsock.sendto('PONG'.encode(), client)
                    clients_list.append(client)
                    i += 1
                    print(i)
        except socket.timeout:
            pass
        except Exception as e:
            print(f"Error occurred: {e}")
            break

    if i == 3:
        if clients_are_the_same(clients_list):
            open_tcp_port(host, tcpport)


if __name__ == '__main__':
    print("[%s] Server started...UDP port sequence: %s, TCP port to open: %s ... \n" % (gettime(), UDP_PORTS, TCP_PORT))

    while True:
        run(HOST, TCP_PORT)

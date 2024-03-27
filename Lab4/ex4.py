#!/usr/bin/env python

import socket
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2901

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

while True:
    data, address = sock.recvfrom(4096)
    equation = data.decode()
    result = eval(equation)  # Calculate the result

    print('[%s] Received %s bytes from client %s. Data: %s' % (
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, equation))

    result_str = str(result)
    sock.sendto(result_str.encode(), address)  # Send the result back to the client
    print('[%s] Sent %s bytes back to client %s.' % (
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(result_str), address))

sock.close()

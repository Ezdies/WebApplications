#!/usr/bin/env python

import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2901

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
        sock.bind((HOST, PORT))
except socket.error as msg:
        print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

print ("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:

        data, address = sock.recvfrom(4096)
        
        print ('[%s] Received %s bytes from client %s. Data: %s' % (
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:
            sent = sock.sendto(data, address)
            print ('[%s] Sent %s bytes bytes back to client %s.' % (
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()
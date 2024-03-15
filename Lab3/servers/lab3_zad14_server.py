#!/usr/bin/env python

import socket, select, sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    txt = txt.decode()
    s = len(txt.split(";"))
    if s != 7:
        return b"BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad14odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try :
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except :
                return b"BAD_SYNTAX"
            if src_port == 46408 and dst_port == 39089 and data == "hello :)":
                return b"TAK"
            else:
                return b"NIE"
        else:
            return b"BAD_SYNTAX"


HOST = '0.0.0.0'
PORT = 2900

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))


try:
    while True:

        data, address = sock.recvfrom(1024)
        print ('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            answer = check_msg_syntax(data)
            sent = sock.sendto(answer, address)
            print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()

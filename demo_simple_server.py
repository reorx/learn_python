#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import base64
import time

from logging_config import sock_log, data_log, dict_config


dict_config()

# Symbolic name meaning the local host
HOST = ''
# Arbitrary non-privileged port
PORT = 24069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    print 'e', type(e), dir(e)
    sock_log.error('Bind failed. code: %s, message: %s', e.errno, e[1])
    sys.exit(1)
sock_log.info('Socket bind complete, port %s', PORT)
s.listen(1)
sock_log.info('Socket now listening')

# Accept the connection once (for starter)
(conn, addr) = s.accept()
sock_log.info('Connected with %s:%s', addr[0], addr[1])

while True:
    # RECEIVE DATA
    data = conn.recv(1024)
    data_log.info('Receive data: %s | %s', data, repr(data))

    if data == '':
        data_log.info('Terminate on empty string')
        break

    if data == 'QUIT':
        conn.send('QUIT')                  # Acknowledge
        break                              # Quit the loop
    else:
        #reply = 'Encrypted: %s' % base64.b64encode(data)
        reply = 'Encrypted: %s' % data

    # SEND REPLY
    if data.startswith('sleep'):
        data_log.info('sleep 5 before send')
        time.sleep(5)
    conn.send(reply)

# if e.errno != errno.ECONNRESET:
conn.close()  # When we are out of the loop, we're done, close
s.close()

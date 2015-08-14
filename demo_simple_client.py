#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from logging_config import sock_log, data_log, dict_config


dict_config()

HOST = ''
PORT = 24069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_log.info('Socket created, port %s', PORT)

s.connect((HOST, PORT))
sock_log.info('Connected to server, port %s', PORT)

while True:
    command = raw_input('Enter your command: ')
    s.send(command)
    reply = s.recv(1024)
    if reply == 'QUIT':
        data_log.info('Got quit, break')
        break
    data_log.info('Got reply: %s', reply)

s.close()
sock_log.info('Close socket')

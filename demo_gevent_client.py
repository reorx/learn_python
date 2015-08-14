#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import time
import gevent
import socket
from functools import partial

from logging_config import sock_log, data_log, dict_config


dict_config()

HOST = ''
PORT = 24069


def get_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_log.info('Socket created, port %s', PORT)
    return s


def connect_socket(s):
    s.connect((HOST, PORT))
    sock_log.info('Connected to server, port %s', PORT)


def send_command(s, cmd):
    s.send(cmd)
    reply = s.recv(1024)
    data_log.info('Got reply: %s', reply)


# main

s = get_socket()
connect_socket(s)

#commands = ['a', 'b', 'c', 'd']
commands = ['sleep', 'a']

for i in commands:
    gthreads = []
    print 'spawn', i
    #time.sleep(0.1)
    g = gevent.spawn(
        partial(send_command, s, i)
    )
    gthreads.append(g)

gevent.joinall(gthreads)

s.close()
sock_log.info('Close socket')

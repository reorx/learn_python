#!/usr/bin/env python
# coding: utf-8

import logging
from tornado.ioloop import IOLoop
from tornado import gen, log
from tornado.websocket import websocket_connect


io_loop = IOLoop.instance()


ws_url = 'ws://localhost:3000/ws'


@gen.coroutine
def start_ws():
    conn = yield websocket_connect(ws_url)
    while True:
        logging.info('!Read message')
        #read_future = conn.read_message()
        #try:
        #    result = yield gen.with_timeout(timedelta(seconds=1), future)
        #    break
        #except gen.TimeoutError:
        #    print('tick')

        msg_str = yield conn.read_message()
        logging.info('!Got message, %s', msg_str)


io_loop.add_callback(start_ws)


if __name__ == "__main__":
    log.enable_pretty_logging()
    logging.basicConfig(level=logging.DEBUG)
    io_loop.start()

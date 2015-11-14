#!/usr/bin/env python
# coding: utf-8

import logging
from tornado import websocket, web, ioloop, log
import json

cl = []


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)
        logging.info("A client connected.")

    def on_close(self):
        if self in cl:
            cl.remove(self)
        logging.info("A client disconnected")


app = web.Application([
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    log.enable_pretty_logging()
    logging.basicConfig(level=logging.DEBUG)
    app.listen(3000)
    ioloop.IOLoop.instance().start()

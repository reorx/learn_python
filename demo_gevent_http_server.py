#!/usr/bin/python

"""WSGI server example"""
from __future__ import print_function
import gevent
from gevent.pywsgi import WSGIServer


def application(env, start_response):
    print(env['PATH_INFO'])
    if env['PATH_INFO'] == '/':
        gevent.sleep(5)
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"sleep 5"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b'<h1>Not Found</h1>']


if __name__ == '__main__':
    print('Serving on 8888...')
    WSGIServer(('', 8888), application).serve_forever()

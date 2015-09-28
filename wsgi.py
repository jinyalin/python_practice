#!/usr/bin/python
"""Replica of icanhazepoch.com - WSGI Style"""
from time import time
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
def epoch_app(environ, start_response):
    setup_testing_defaults(environ)
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    return ["hello world".encode('UTF-8')]
if __name__ == '__main__':
    make_server('0.0.0.0', 8000, epoch_app).serve_forever()

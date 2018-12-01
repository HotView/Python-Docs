'''
Created on Aug 2, 2015

@author: Burkhard
'''

from socketserver import BaseRequestHandler, TCPServer

class RequestHandler(BaseRequestHandler):
    # override base class handle method
    def handle(self):
        print('Server connected to: ', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b'Server received: ' + rsp)

def startServer():
    serv = TCPServer(('localhost', 24000), RequestHandler)
    serv.serve_forever()


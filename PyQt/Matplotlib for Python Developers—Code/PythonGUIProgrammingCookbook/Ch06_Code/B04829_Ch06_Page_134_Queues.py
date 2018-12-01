'''
Created on Aug 1, 2015

@author: Burkhard
'''

from socket import socket, AF_INET, SOCK_STREAM

def writeToScrol(inst):
    print('hi from Queue', inst)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 24000))
    for idx in range(10):
        sock.send(b'Message from a queue: ' + bytes(str(idx).encode()) )
        recv = sock.recv(512).decode()
        inst.guiQueue.put(recv)      
    inst.createThread(6)

#!/usr/bin/python3

from socket import *
from struct import *

clientSocket = socket()
clientSocket.connect(('vortex.labs.overthewire.org', 5842))
res0 = clientSocket.recv(4)
res1 = clientSocket.recv(4)
res2 = clientSocket.recv(4)
res3 = clientSocket.recv(4)
unsigneds = (
    unpack('I', res0)[0],
    unpack('I', res1)[0],
    unpack('I', res2)[0],
    unpack('I', res3)[0]
    )
print(unsigneds)
u_sum = sum(unsigneds).to_bytes(8, 'little')
print(u_sum)
clientSocket.send(pack('BBBB', *u_sum[0:4]))
response = clientSocket.recv(1024)
print(response.decode('utf-8'))
clientSocket.close()
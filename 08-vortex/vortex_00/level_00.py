#!/usr/bin/python3

from socket import *
from struct import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('vortex.labs.overthewire.org', 5842))
unsigneds = []
for i in range(0,4):
    unsigned = clientSocket.recv(4)
    unsigneds.append(unpack('I', unsigned)[0])
print(unsigneds)
u_sum = sum(unsigneds).to_bytes(8, 'little')
print(u_sum)
clientSocket.send(pack('BBBB', *u_sum[0:4]))
response = clientSocket.recv(1024)
print(response.decode('utf-8'))
clientSocket.close()
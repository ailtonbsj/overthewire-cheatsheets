#!/usr/bin/python3
from socket import *
from struct import *

clientSocket = socket()
clientSocket.connect(('vortex.labs.overthewire.org', 5842))
response = clientSocket.recv(16)
unsigneds = unpack('IIII', response)
clientSocket.send(pack('I', sum(unsigneds)))
response = clientSocket.recv(1024)
print(response)
clientSocket.close()
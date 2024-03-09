#!/usr/bin/python3
from socket import *

serverName = 'localhost'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(b'GET / HTTP/1.1\nHost: localhost:8080\n\n\n')
response = clientSocket.recv(1024)
print('From Server: ', response)
clientSocket.close()

#!/bin/python3

import binascii

# ASCII to Binary
text = b'Hello World!'
res = bin(int(binascii.hexlify(text), 16))
print(res)

# Binary to ASCII
binary = '01000101 01001011 01001011 01101100 01010100 01000110 00110001 01011000 01110001 01110011 00001010'.replace(' ', '')
n = int(binary, 2)
res = binascii.unhexlify('%x' % n)
print(res)

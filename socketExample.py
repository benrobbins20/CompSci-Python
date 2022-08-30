import socket as skt
import time 

s = skt.socket(skt.AF_INET,skt.SOCK_STREAM)

s.connect(("10.x.x.x",4444))
s.send(b"[+] Connection established, closing in ten seconds")
for i in range(1,11):
    counter = 11 - i
    s.send(b'...')
    s.send(str(counter).encode('utf-8'))
    time.sleep(1)
s.send(b'\nclosing connection\n')
s.close()

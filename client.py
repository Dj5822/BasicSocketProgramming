import socket

s = socket.socket()

port = 12000

s.connect(('localhost', port))

print(s.recv(1024))

s.close()
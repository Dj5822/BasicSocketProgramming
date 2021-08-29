import socket

port = 12000

s = socket.socket()
print("socket successfully created.")

s.bind(('', port))
print("socket binded to {}".format(port))

s.listen(5)
print("Server stated listening localhost: {}".format(port))

while True:
    c, addr = s.accept()
    print("Got connection from {}".format(addr))

    c.send('Random message'.encode())

    c.close()

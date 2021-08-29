import socket

server_ip = 'localhost'
port = 12000
s = socket.socket()

# Bind and start the server.
s.bind((server_ip, port))
s.listen(5)
print("Server started listening {}: {}".format(server_ip, port))

while True:
    c, addr = s.accept()
    print("Got connection from {}".format(addr))

    # Send data to the client.
    c.send('Random message'.encode())

    c.close()

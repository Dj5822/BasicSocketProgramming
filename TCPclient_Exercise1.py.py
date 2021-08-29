import socket

server_ip = 'localhost'
port = 12000
s = socket.socket()

try:
    s.connect((server_ip, port))
    print("Connection established to server {}: {}".format(server_ip, port))

    print(s.recv(1024))

    s.close()
except ConnectionRefusedError:
    print("Error: start the server first.")



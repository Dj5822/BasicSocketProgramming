import socket

server_ip = 'localhost'
port = 12000
s = socket.socket()

try:
    # Connect to the server.
    s.connect((server_ip, port))
    print("Connection established to server {}: {}".format(server_ip, port))

    # Receive data from the server.
    print(s.recv(1024))

    s.close()
except ConnectionRefusedError:
    print("Error: start the server first.")



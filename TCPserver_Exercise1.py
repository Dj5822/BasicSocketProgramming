import socket

server_ip = 'localhost'
port = 12000
input_file_name = "Jellyfish.mp4"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and start the server.
s.bind((server_ip, port))
s.listen(5)
print("Server started listening {}: {}".format(server_ip, port))

while True:
    c, addr = s.accept()
    print("Got connection from {}".format(addr))

    # read bytes from the file.
    with open(input_file_name, "rb") as file:
        data = b''.join(file.readlines())
        file.close()

    # split bytes into groups of 1024.
    start = 0
    end = 1024
    output_list = []
    while len(data) > end:
        output_list.append(data[start:end])
        start = end
        end += 1024
    output_list.append(data[start:end])

    # Send data to the client.
    for output in output_list:
        c.send(output)
    c.send(b'')

    c.close()

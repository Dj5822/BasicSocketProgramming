import socket

server_ip = 'localhost'
port = 12000
output_file_name = "receivedVid.mp4"
s = socket.socket()

try:
    # Connect to the server.
    s.connect((server_ip, port))
    print("Connection established to server {}: {}".format(server_ip, port))

    # Receive data from the server.
    video_data = []
    incoming_data = None

    # continue receiving data until we get the termination signal.
    while incoming_data != b'':
        incoming_data = s.recv(1024)
        if incoming_data != b'':
            video_data.append(incoming_data)

    # write bytes back into an mp4 file.
    with open(output_file_name, "wb") as file:
        file.write(b''.join(video_data))
        file.close()

    s.close()
except ConnectionRefusedError:
    print("Error: start the server first.")



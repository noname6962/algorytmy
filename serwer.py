import socket

IP_server = "127.0.0.1"
PORT_server = 4444

# Create a socket
serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind((IP_server, PORT_server))
serwer.listen(2)
client, address = serwer.accept()
print("Connected to client", address)

while True:
    data=client.recv(1024)
    print(data.decode("utf-8"))
    client.send(data)



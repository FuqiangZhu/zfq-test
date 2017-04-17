
import socket

client = socket.socket()
client.connect(('localhost', 5050))
client.send(b'Hello World')
data = client.recv(1024)
print(data)
client.close()

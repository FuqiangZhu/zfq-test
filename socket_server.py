
import socket

server = socket.socket()
server.bind(('localhost', 5050))
server.listen()
conn, addr = server.accept()
print(conn, addr)
data = conn.recv(1024)
print(data)
conn.send(data.upper())

server.close()

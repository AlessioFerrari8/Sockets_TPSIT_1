import socket
from cripto import decifra

host = "127.0.0.1" #192.168.?.? - localhost - 127.0.0.1 - 0.0.0.0
port = 6767 # PORTA IN ASCOLTO

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP IPv4 
socket = (host, port)
server_socket.bind(socket)
server_socket.listen() #socket in ascolto

conn, ip = server_socket.accept()
#abbiamo la connessione (conn)
bytes = conn.recv(1024)
print(decifra(bytes))


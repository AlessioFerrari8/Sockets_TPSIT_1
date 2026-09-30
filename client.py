import socket
import threading 
import time
from cripto import cifra


host = "127.0.0.1"
port = 6767 # PORTA A CUI CONNETTERSI

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client_socket.bind() non serve a nulla

client_socket.connect((host, port))
client_socket.sendall(cifra("Amedeo è goat"))


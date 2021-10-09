import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
  clientsocket.connect((socket.gethostname(), 4001))
  clientsocket.sendall(b'Hello, world')

  data = clientsocket.recv(1024)

print('Received', repr(data))
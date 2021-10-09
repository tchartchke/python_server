import socket

# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
  
  # bind the socket to a public host, and a well-known port
  serversocket.bind((socket.gethostname(), 4001))
  print("Socket Opened. Listening on 4001")
  
  # become a server socket
  serversocket.listen(5)
  
  # accept connections from outside
  (clientsocket, address) = serversocket.accept()
  with clientsocket:
    print("Connected at", address)
    while True:
  
      #receive data from client
      data = clientsocket.recv(1024)
      print("Raw Data:", data)
      if not data: 
        print("No Data")
        break 
  
      #send data back to client
      clientsocket.sendall(data)
        
import socket

# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
  # causes the port to be released immediately after the socket is closed
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # bind the socket to a public host, and a well-known port
  HOST = '0.0.0.0'
  PORT = 8000
  
  serversocket.bind((HOST, PORT))

  # become a server socket
  serversocket.listen()
  print('Listening on port %s ...' % PORT)
  
  while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    with clientsocket:
    
      #receive data from client
      request = clientsocket.recv(1024).decode()
      print("Request:\n", request)
  
      #getting cont text from html
      content = ''
      with open('index.html', 'r') as file:
        content = file.read()

      #send data back to client
      response = 'HTTP/1.0 200 OK\n\n' + content
      clientsocket.sendall(response.encode())
      
      
#!/usr/bin/env python3

#   $ chmod +x myFile.py      marks as executable

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost) => socket.gethostname()
PORT = 65432        # Port to listen on (non-privileged ports are > 1023) => 80 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Socket Opened. Listening")
    s.listen()
    conn, addr = s.accept() # new socket object representing the connection and a tuple holding the address of the client: (host, port)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

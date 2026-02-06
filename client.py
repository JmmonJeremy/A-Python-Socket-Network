"""Project Outline"""
"""Files"""  # one program for the client (THIS ONE) and one program for the server 
"""Server""" #1 listens for connections on the ip address of (localhost 127.0.0.1) and port number () #2 processes request & sends a response back to client
#3 runs inside a loop that continuously accepts new connections so that the server socket remains open to consistently handle disconnecting & connecting
"""Client""" #1 connects to the waiting server #2 sends request message to the server #3 number, #4 v_date #5 week_number
"""Stretch Challenge""" #1 Server responds to 3 requests types (UPLOAD, DOWNLOAD, LIST)

"""CODE to IMPORT libraries used"""
import socket

"""CODE to set up the CLIENT"""
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6000  # The port used by the server

# with statement - so won't need to call client.close()
# AF_INET is (IPv4) - so bind expects (host, port) & SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b"Hello, world")
    data = client.recv(1024)

print(f"Received {data!r}")
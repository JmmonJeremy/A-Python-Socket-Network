"""Project Outline"""
"""Files"""  # one program for the client (THIS ONE) and one program for the server 
"""Server""" #1 listens for connections on the ip address of (localhost 127.0.0.1) and port number () #2 processes request & sends a response back to client
#3 runs inside a loop that continuously accepts new connections so that the server socket remains open to consistently handle disconnecting & connecting
"""Client""" #1 connects to the waiting server #2 sends request message to the server
"""Stretch Challenge""" #1 Server responds to 3 requests types (UPLOAD, DOWNLOAD, LIST)

"""CODE to IMPORT libraries used"""
import socket
import threading
import os

"""CODE to set up the SERVER"""
# constants
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 6000  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 4096 # 4 KB - common OS memory page size
FILES_DIR = "uploaded_files" # folder for uploaded files
# variable
shutdown_flag = False

os.makedirs(FILES_DIR, exist_ok=True)

def handle_client(conn, addr):
    global shutdown_flag
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            # Converts bytes into a Python string
            request = conn.recv(BUFFER_SIZE).decode() 
            # recv() returns b'' when client closes connection to signal closed
            if not request:
                break
            # Splits the command into separate parts to be used
            parts = request.split(' ', 1) 
            # Selects the first word, which is the command
            command = parts[0] 
            # Uses command to determine the action
            if command == "LIST":
                files = os.listdir(FILES_DIR)
                # Takes the list of directory filenames and separates them into one name per line
                response = "\n".join(files) if files else "No files available."
                # Sends the list as the response
                conn.sendall(response.encode())
            elif command == "UPLOAD":
                # Extracts the filename
                filename = os.path.basename(parts[1])
                # Creates the path for the file
                filepath = os.path.join(FILES_DIR, filename)
                # Sends READY signal message to client as bytes
                conn.sendall(b"READY")
                # w is write mode and b is binary mode (write binary)
                with open(filepath, "wb") as file:
                    while True:
                        # Receives a 4 KB chunk of the file
                        data = conn.recv(BUFFER_SIZE)
                        # Stop signal sent from client for end of file
                        if b"EOF" in data:
                            # Write everything before the EOF
                            file.write(data.replace(b"EOF", b""))
                            break
                        file.write(data)
                # Sends the signal message to the client for a successful upload
                conn.sendall(b"UPLOAD COMPLETE")
            elif command == "DOWNLOAD":
                # Extracts the filename
                filename = parts[1]
                # Creates the path for the file
                filepath = os.path.join(FILES_DIR, filename)
                # Makes sure file exists
                if os.path.exists(filepath):
                    # Sends READY signal message to client as bytes
                    conn.sendall(b"READY")
                    # r is read mode and b is binary mode (read binary)
                    with open(filepath, "rb") as file:
                        # If chunk of file is empty it stops while loop
                        while chunk := file.read(BUFFER_SIZE):
                            conn.sendall(chunk)
                    # Stop signal sent from client for end of file
                    conn.sendall(b"EOF")
                else:
                    conn.sendall(b"FILE NOT FOUND")
            elif command == "SHUTDOWN":
                conn.sendall(b"SERVER SHUTTING DOWN")
                shutdown_flag = True
                break
            # Covers incorrect command entries
            else:
                conn.sendall(b"INVALID COMMAND")
    print(f"[DISCONNECTED] {addr}")

def start_server():
    # global tags this variable as the one at the top of the file
    global shutdown_flag
    # with statement - so won't need to call server.close()
    # AF_INET is (IPv4) - so bind expects (host, port) & SOCK_STREAM is the socket type for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
        server.bind((HOST, PORT))
        server.listen()
        server.settimeout(1) 
        print(f"Server listening on port {PORT}")
        try:
            while not shutdown_flag:
                try:
                    conn, addr = server.accept()
                except socket.timeout:
                    continue  # loop again to check shutdown_flag
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
        except KeyboardInterrupt:
            print("\nServer manually stopped with CTRL + C.")
    print("Server has shut down.")
# In every Python file, there is a built-in variable called __name__
# If the file is run directly (like python server.py), Python will set __name__ = "__main__"
# If the file is imported as a module in another Python file (like import server), Python will set __name__ = "server"
if __name__ == "__main__":
    # If server.py file is being run directly start_server() runs & the server starts listening for clients
    start_server()
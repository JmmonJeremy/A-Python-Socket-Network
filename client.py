"""Project Outline"""
"""Files"""  # one program for the client (THIS ONE) and one program for the server 
"""Server""" #1 listens for connections on the ip address of (localhost 127.0.0.1) and port number () #2 processes request & sends a response back to client
#3 runs inside a loop that continuously accepts new connections so that the server socket remains open to consistently handle disconnecting & connecting
"""Client""" #1 connects to the waiting server #2 sends request message to the server #3 number, #4 v_date #5 week_number
"""Stretch Challenge""" #1 Server responds to 3 requests types (UPLOAD, DOWNLOAD, LIST)

"""CODE to IMPORT libraries used"""
import socket
import os

"""CODE to set up the CLIENT"""
# constants
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6000  # The port used by the server
BUFFER_SIZE = 4096 # 4 KB - common OS memory page size

# Ensures the user chooses a number from the menu
def validate_menu_choice(prompt: str, min_value: int = 1, max_value: int = 7) -> int:
    while True:
        user_input = input(prompt).strip()
        if not user_input.isdigit():
            print(f"ERROR! Please enter a number from the menu ({min_value}-{max_value}).")
            continue
        number = int(user_input)
        if not (min_value <= number <= max_value):
            print(f"ERROR! Please enter a number from the menu ({min_value}-{max_value}).")
            continue
        return number

def upload_file(sock, filename):
    # Converts Python string into bytes default is UTF-8 (8-bit blocks)
    sock.sendall(f"UPLOAD {filename}".encode())
    response = sock.recv(BUFFER_SIZE)
    if response == b"READY":
        # r is read mode and b is binary mode (read binary)
        with open(filename, "rb") as file:
            # Reading the file from disk into memory & sending it
            while chunk := file.read(BUFFER_SIZE):
                sock.sendall(chunk)
        sock.sendall(b"EOF")
        # Recieves final signal & prints response
        confirmation = sock.recv(BUFFER_SIZE)
        if confirmation == b"UPLOAD COMPLETE":
            print("\nYour file has been successfully uploaded.")
        else:
            print("\nThe file upload failed.")  

def download_file(sock, filename):
    # Converts Python string into bytes default is UTF-8 (8-bit blocks)
    sock.sendall(f"DOWNLOAD {filename}".encode())
    response = sock.recv(BUFFER_SIZE)
    if response == b"READY":
        # w is write mode and b is binary mode (write binary)
        with open(filename, "wb") as file:
            while True:
                data = sock.recv(BUFFER_SIZE)
                if b"EOF" in data:
                    # Write everything before the EOF
                    file.write(data.replace(b"EOF", b""))
                    break
                file.write(data)
        print("\nDownload complete.")
    else:
        print(response.decode())

def list_files(sock):
    sock.sendall(b"LIST")
    print("\nList of Uploaded Files:")
    print(sock.recv(BUFFER_SIZE).decode())

"""CODE to connect the CLIENT"""
# with statement - so won't need to call client.close() - happens when block ends
# AF_INET is (IPv4) - so bind expects (host, port) & SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    
    """CODE to CREATE the USER INTERFACE"""
    # Create a menu for server requests - #1 LIST, #2 UPLOAD, #3 DOWNLOAD, #4 DISCONNECT CLIENT, #5 SERVER SHUTDOWN
    choice = None #INTERFACE#####################################################################################
    while choice != 4 or choice != 5:
        print("\nSelect an option:")
        print("1) List uploaded files")
        print("2) Upload a file")
        print("3) Download a file")
        print("4) End your connection")
        print("5) Shut the server down") 
        choice = validate_menu_choice(("   ->  "), 1, 5)
        print("   ‾‾‾")

        """CODE to PERFORM selected ACTIONS"""
        #CODE to send a LIST request to the server
        if choice == 1: #LIST###############################################################################################       
            list_files(client)
        # CODE to UPLOAD a file to the server
        elif choice == 2: #UPLOAD###########################################################################################
            filename = input("(If the file is in a different location include the path to the file.)\nPlease enter the name of the file to be uploaded: ")   
            upload_file(client, filename)
        # CODE to DOWNLOAD a file from the server
        elif choice == 3: #DOWNLOAD#########################################################################################
            filename = input("Please enter the name of the file to be downloaded: ")
            download_file(client, filename)
        # CODE to END the client's connection to the server
        elif choice == 4: #DISCONNECT###########################################################################################
            print("You have successfully disconnected from the server.\n")
            # Exit the while loop and complete the with block to close the client connection
            break
        # CODE to SHUTDOWN the server
        elif choice == 5: #SHUTDOWN###########################################################################################
            client.sendall(b"SHUTDOWN")
            response = client.recv(BUFFER_SIZE)          
            print(response.decode() + ". . .")
            print("You are now disconnected from the server.\n")
            # Exit the while loop and complete the with block to close the client connection
            break

  
   
   
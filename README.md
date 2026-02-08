# Python Socket, Threading, & OS Client-Server File Transfer System

This is a client–server file transfer system using Python’s socket networking library for TCP communication, threading library to handle multiple clients at the same time, and os library to handle files and manage the directory. The server is set up to handle an UPLOAD request to upload any file, a LIST request to list all uploaded files, and a DOWNLOAD request to download any file that has been uploaded.

## Instructions for Build and Use

[Software Demo](Put_Your_Video_Link_Here)

#### Steps to build and/or run the software:

1. Go to the official Python website https://www.python.org/downloads/ and click link to Download Python 3.10 or newer
2. Then double-click the download installer, check the box that says Add Python to PATH, and click Install Now
3. Install the Microsoft Python language support extension in VSCode to make the play button available
4. Create a python file for the server and import socket, threading, and os at the top of the file
5. In the python server file insert the code for running the server
6. Create a python file for the client and import socket and os at the top of the file
7. In the python client file insert the code for running the server

#### Instructions for using the software:

1. In VSCode go to the server.py file in your project folder open the terminal at the bottom.
2. Press the dropdown arrow on the play button in the top right corner of the screen and select "Run Python File in Dedicated Terminal" from the options.
3. In VSCode change to the client.py file in your project folder and repeat the selection of "Run Python File in Dedicated Terminal" for the play option.
4. Alternatively, enter python server.py in one open terminal. Then open another terminal and enter python client.py.
5. Use the provided menu in the terminal to list, download, and upload files.
6. To open and use multiple clients, while in the client.py file repeat the selection of "Run Python File in Dedicated Terminal" from the python play button option.
7. Alternatively, to open and use multiple clients, enter python client.py in other open terminals.
8. To disconnect a client from the server enter 4 from the main menu options.
9. To shut down the server enter 5 from the main menu options or enter CTRL + C in the terminal running the server.
    
## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Visual Studio Code
* Python 3.13.7 64-bit
* Python socket library
* Python threading library
* Python os library
* Git / GitHub

## Useful Websites to Learn More

I found these websites useful in developing this software:

### Visual Studio Code :
* [Visual Studio Code & GitHub](https://code.visualstudio.com/docs/sourcecontrol/overview)

### Python :
* [Python Functions Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Python Main Tutorial](https://docs.python.org/3.13/tutorial/modules.html#executing-modules-as-scripts)
* [Python Bold & Underlined Text](https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/effects/#cheat-sheet)
* [Python Color & Reset Text Style](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
* [Python Docs With Statement](https://docs.python.org/3/reference/compound_stmts.html#with)
* [Python Docs Join](https://docs.python.org/3.13/library/stdtypes.html#str.join)
* [Python Docs Split](https://docs.python.org/3/library/stdtypes.html#str.split)
* [Python Docs Bytes](https://docs.python.org/3.13/library/stdtypes.html#bytes-objects)
* [Python Docs Open](https://docs.python.org/3.13/library/functions.html#open)
* [Python := Operator](https://realpython.com/python-walrus-operator/)
* [Python Underscore](https://www.geeksforgeeks.org/python/underscore-_-python/)  

### Socket Library :
* [Socket Tutorial](https://realpython.com/python-sockets/)
* [Socket Docs socket](https://docs.python.org/3.13/library/socket.html#socket.socket)
* [Socket Docs recv](https://docs.python.org/3.13/library/socket.html#socket.socket.recv)
* [Socket Docs sendall](https://docs.python.org/3.13/library/socket.html#socket.socket.sendall) 
* [Socket Docs bind](https://docs.python.org/3.13/library/socket.html#socket.socket.bind)
* [Socket Docs listen](https://docs.python.org/3.13/library/socket.html#socket.socket.listen)
* [Socket Docs accept](https://docs.python.org/3.13/library/socket.html#socket.socket.accept)
* [Socket Docs decode](https://docs.python.org/3.13/library/stdtypes.html#bytes.decode)

### Threading Library :
* [Threading Docs Page](https://docs.python.org/3.13/library/threading.html)
* [Threading Docs Thread](https://docs.python.org/3.13/library/threading.html#threading.Thread)
* [Threading Tutorial](https://realpython.com/intro-to-python-threading/)

### OS Library :
* [OS Docs Page](https://docs.python.org/3.13/library/os.html)
* [OS Docs listdir](https://docs.python.org/3/library/os.html#os.listdir)
* [OS Docs Path Basename](https://docs.python.org/3.13/library/os.path.html#os.path.basename)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] I plan on fixing the 5th Menu option to shut down the server using threads instead of a shutdown flag and timeout - so other client threads will be closed instead of keeping a connection until the close
* [ ] I plan on using the file size to determine when a file is done uploading or downloading so that a file with the keyword EOF in it will not cause a problem
* [ ] I plan to make the option to close the server only accessable to a super user with a password

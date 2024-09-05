import socket
import sys

# Create a connection to the server application on port 65432
tcp_socket = socket.create_connection(('localhost', 65432))

try:
    print("You can leave at any time by sending exit")
    while True:
        user_input = input(" >> ")
        if user_input == "exit":
            break
        data = user_input.encode('utf-8')
        tcp_socket.sendall(data)
finally:
    tcp_socket.close()
    print("Exiting...")
    sys.exit(0)
import socket

# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost and port 65432
server_address = ('localhost', 65432)
tcp_socket.bind(server_address)

# Listening to one connection
tcp_socket.listen(1)

while True:
    print("Waiting for a connection")
    connection, client_address = tcp_socket.accept()
    try:
        print(f"Connected to client IP: {client_address}")
        # Receive and print data 1024 bytes at a time, as long as the client is sending something
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received {data}")
            if not data:
                break
    finally:
        connection.close()
        print("Connection closed")

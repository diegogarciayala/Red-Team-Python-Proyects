import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        message = input("Text your message here: ")
        client_socket.sendall(message.encode('utf-8'))

        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Server >> {data.decode('utf-8')}")
finally:
    client_socket.close()
    print("Server connection closed")

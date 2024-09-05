import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
server_socket.bind(server_address)

print("Waiting for a connection...")

connection, client_address = server_socket.accept()
print(f'Connected by: {client_address[0]}:{client_address[1]}')

try:
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f'\nClient >> {data.decode('utf-8')}\n')

    message = input('\nEnter your message: ')
    connection.send(message.encode('utf-8'))

finally:
    connection.close()
    server_socket.close()
    print('Server closed.')

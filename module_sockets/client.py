import socket


def start_client():
    host = socket.gethostname()
    port = 8080
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Type your text:\n")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Received from server:", data)
        message = input("Type your text:\n")

    client_socket.close()


if __name__ == '__main__':
    start_client()

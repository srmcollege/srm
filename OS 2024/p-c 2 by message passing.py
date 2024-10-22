import socket

def client_program():
    host = socket.gethostname()
    port = 4000
    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received from server:", data)

    client_socket.close()
    print("Connection closed.")

if __name__ == '__main__':
    client_program()

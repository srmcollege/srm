import socket
import time

def server_program():
    host = socket.gethostname()
    port = 4000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Waiting for client...")

    conn, address = server_socket.accept()
    print("Connection from:", address)

    messages = ["Message 1", "Message 2", "Message 3"]
    for msg in messages:
        print("Sending:", msg)
        conn.send(msg.encode())
        time.sleep(1)

    conn.close()
    print("Connection closed.")

if __name__ == '__main__':
    server_program()

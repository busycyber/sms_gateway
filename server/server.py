import socket
import threading
import pickle

SERVER_HOST = '192.168.0.88'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 1024

def handle_client(client_socket, client_address):
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break

        data = pickle.loads(data)

        string_data = data['string']
        list_data = data['list']

        print(f"Received string: {string_data}")
        print(f"Received list: {list_data}")

    client_socket.close()

def start_server():
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen()

    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    while True:
        client_socket, client_address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

start_server()

import socket
def client_program(host):
    port = 5234  
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Connected to server.")

    filename = 'example.txt'  # The file you want to send
    with open(filename, 'rb') as f:
        print("Sending file...")
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    print("File sent successfully.")
    client_socket.close()

if __name__ == '__main__':
    client_program('192.168.56.1')

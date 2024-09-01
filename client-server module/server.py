import socket
def server_program():
    host = '0.0.0.0'  
    port = 5234
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port", port)

    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    with open('received_file.txt', 'wb') as f:
        print("Receiving file...")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("File received successfully.")
    conn.close()
    server_socket.close()

def get_ip_address():
    hostname = socket.gethostname()  
    ip_address = socket.gethostbyname(hostname)  
    return ip_address

if __name__ == '__main__':
    ip = get_ip_address()
    print(f"Your IP address is: {ip}")
    server_program()
    



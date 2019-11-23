import socket
from threading import Thread



def server():
    #configuration of host and port
    host = socket.gethostname()
    port = 1234  

    server = socket.socket()  # get socket instance instance
    server.bind((host, port))

    server.listen(2)
    conn, address = server.accept()  # accept new connection
    while True: #continuous loop
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')

        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection



server() #function call

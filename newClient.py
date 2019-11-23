import socket


def client():
    host = socket.gethostname()  
    port = 1234 

    client = socket.socket() 
    client.connect((host, port))  # connect to the server

    message = input("-> ")
    while message != 'bye':

         client.send(message.encode())  # send message
         data = client.recv(1024).decode()
         print('Received from server: ' + data) 
         message = input("-> ")

    client_socket.close()  # close the connection



client() #function call

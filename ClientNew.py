import socket, threading
import select
import sys


import socket, threading

def send():
    while True:
        message = raw_input('\nMe > ')
        cli_sock.send(message)

def receive():
    while True:
        our_name = cli_sock.recv(1024)
        data = cli_sock.recv(1024)
        
        print('\n' + str(our_name) + ' > ' + str(data))

if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connect
    HOST = 'localhost'
    PORT = 4096
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')
    display_name = raw_input('Enter your name to enter the chat > ')
    cli_sock.send(display_name)
    
    thread_send = threading.Thread(target = send)
    thread_send.start()
    
    thread_receive = threading.Thread(target = receive)
    thread_receive.start()


def accept():
    while True:
        client, add_client = server.accept()
        display_name = client.recv(4096)
        lost_connection.append((display_name, client))
        print('%s is now connected' %display_name)

def broadcast(data, connection):
    while True:
        for client in client_list:
        #if client != connection:
            try:
                data = client.recv(4096)
                if data:
                    userB(client_list[i][1],client_list[i][0], data)
                    #client.send(message)
            except Exception as x:
                print (x.message)
                break
    
    #except:
    #client.close()
    #remove(client)
def userB(cs_sock, our_name, message):
    for i in range(len(client_list)):
        if (client_list[i][1] != cs_sock):
            client_list[i][1].send(our_name)
            client_list[i][1].send(message)

if __name__ == "__main__":
    client_list = []


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.listen(1)

thread_ac = threading.Thread(target = accept)
thread_ac.start()

#thread_bs = threading.Thread(target = broadcast)
#thread_bs.start()
#
#if len(sys.argv) != 3:
#   print "Provided Correct Attributes"
#   exit()
#IP_address = str(sys.argv[1])
#port = int(sys.argv[2])

#server.bind((IP_address, port))


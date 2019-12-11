import socket, threading
import sys
import select


def joinChat():
    while True:
        #accept
        cli_sock, cli_add = our_socket.accept()
        display_name = cli_sock.recv(1024)
        client_list.append((display_name, cli_sock))
        print('%s is now connected' %display_name)
        thread_client = threading.Thread(target = sendToAll, args=[display_name, cli_sock])
        thread_client.start()
    select.select([our_socket,], [our_socket,], [], 5)
    if select.error:
        cli_sock.shutdown(2)    # 0 = done receiving, 1 = done sending, 2 = both
        cli_sock.close()
                # connection error event here, maybe reconnect
        print 'connection error'

def sendToAll(display_name, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                print "{0} spoke".format(display_name)
                second_user(cli_sock, display_name, data)
        except Exception as x:
            print(x.message)
            break

def second_users(cs_sock, sen_name, message):
    for client in client_list:
        if client[1] != cs_sock:
            client[1].send(sen_name)
            client[1].send(message)

if __name__ == "__main__":
    client_list = []
    
    # socket
    our_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # bind
    HOST = 'localhost'
    PORT = 4096
    our_socket.bind((HOST, PORT))
    
    # listen
    our_socket.listen(1)
    print('Chat server started on port : ' + str(PORT))
    
    thread_ac = threading.Thread(target = joinChat)
    thread_ac.start()


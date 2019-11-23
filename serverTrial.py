import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 1234))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096).decode()
        if not data: break
        from_client += data
        print(from_client)
        conn.send("I am Jeremy\n".encode('ascii'))
    conn.close()
    print('client disconnected')

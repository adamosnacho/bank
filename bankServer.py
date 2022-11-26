import socket
from threading import Thread

def handleConn(data):
    print(data)
quitMsg = 'quit'
host = socket.gethostname()
port = 5000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server_socket = socket.socket()
server_socket.bind((host, port))
print(myip)

server_socket.listen(2)  # accept new connection
while True:
    conn, address = server_socket.accept()
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data == None:
        print('from connected user: ' + str(address[0])+' ' + eval(str(data))[0])
        if eval(data) == 'usrVal':
            f = open()
        #conn.send(file.encode())  # send data to the client
    conn.close()
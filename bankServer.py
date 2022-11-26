import socket
from threading import Thread
quitMsg = 'quit'
host = socket.gethostname()
port = 6000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server_socket = socket.socket()
server_socket.bind((host, port))
print(myip)

server_socket.listen(2)  # accept new connection
while True:
    conn, address = server_socket.accept()
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data:
        break
    print('from connected user: ' + str(address[0])+' ' + str(eval(str(data))))
    print(eval(data)[0])
    if eval(data)[0] == 'usrVal':
        f = open(eval(data)[1]+'.txt','r')
        password = eval(str(f.read()))[1]
        f.close()
        if password == eval(data)[2]:
            message = 'userValidated'
            conn.send(message.encode())
            print('userValidated')  # send data to the client
        else:
            conn.send('userNOTValidated'.encode())
            print('user not validated')
    if eval(data)[0] == 'usrNew':
        try:
            f = open(eval(data)[1]+'.txt','x')
            f.close()
            f = open(eval(data)[1]+'.txt','w')
            passw = eval(data)[2]
            dt = [0,passw]
            f.write(str(dt))
            f.close()
        except:pass
        #conn.send(file.encode())  # send data to the client
    conn.close()
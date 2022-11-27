import socket
from threading import Thread
quitMsg = 'quit'
host = socket.gethostname()
port = 5000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server_socket = socket.socket()
server_socket.bind((host, port))
print(myip)

server_socket.listen(2)  # accept new connection
conn, address = server_socket.accept()
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data:
        break
    print('from connected user: ' + str(address[0])+' ' + str(eval(str(data))))
    if eval(data)[0] == 'usrVal':
        try:
            f = open(eval(data)[1]+'.txt','r')
            password = eval(str(f.read()))[1]
            f.close()
            if password == eval(data)[2]:
                message = 'userValidated'
                conn.send(message.encode())
                print('[usrVal] userValidated')  # send data to the client
            else:
                conn.send('userNOTValidated'.encode())
                print('[usrVal] user not validated')
        except:conn.send('userNOTValidated'.encode())
    if eval(data)[0] == 'usrNew':
        try:
            f = open(eval(data)[1]+'.txt','x')
            f.close()
            f = open(eval(data)[1]+'.txt','w')
            passw = eval(data)[2]
            dt = [0,passw]
            f.write(str(dt))
            f.close()
            print('[usrNew] created new user')
        except:pass
    if eval(data)[0] == 'admLogin':
        f = open('adminPassword.txt','r')
        if f.read() == eval(data)[1]:
            conn.send('adminGranted'.encode())
        else:
            conn.send('adminNotGranted'.encode())
    if eval(data)[0] == 'bal':
        try:
            f = open(eval(data)[1] + '.txt')
            bal_ = eval(f.read())[0]
            f.close()
            conn.send(str(bal_).encode())
        except:pass
    if eval(data)[0] == 'trans':
        pass
    
conn.close()
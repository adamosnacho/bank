import socket

def client_program():
    host = '192.168.0.63'
    port = 5000  # socket server port number\
    data = ' '



    message = 'ip of conncted user ' + socket.gethostbyname(socket.gethostname())
    createUser = input('create new user? (True/False) --> ')
    if createUser:
        newUsrName = input('[SETUP] new username --> ')
        newPass = input('[SETUP] new password --> ')
        file = open(newUsrName + '.txt','w')
        file.write(newPass)
        file.close()
    username = input('USERNSME --> ')
    password = input('PASSWORD --> ')

    try:
        userFile = open(username + '.txt','r')
        if userFile.read() != password:
            quit('WRONG PASSWORD!')
        userFile.close()
    except:
        quit('NO SUCH USER!')

    client_socket = socket.socket()  # instantiate  # connect to the server
    client_socket.connect((host, port))
    message = ['usrVal',username,password]
    client_socket.send(str(message).encode())  # send message
    client_socket.close()  # close the connection
    message = ''
    while True:
        client_socket = socket.socket()  # instantiate  # connect to the server
        client_socket.connect((host, port))
        print('Received from server: ' + data)  # show in terminal
        message = input("--> ")  # again take input
        client_socket.send(str(message).encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        client_socket.close()  # close the connection

client_program()
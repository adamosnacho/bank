import socket
from getch import getche, getch
host = '192.168.0.63'
port = 5000  # socket server port number
def client_program():
    client_socket = socket.socket()  # instantiate  # connect to the server
    client_socket.connect((host, port))


    message = 'ip of conncted user ' + socket.gethostbyname(socket.gethostname())
    createUser = input('create new user? (y/n) --> ')
    if createUser == 'y':
        newUsrName = input('[SETUP] new username --> ')
        newPass = input('[SETUP] new password --> ')
        client_socket.send(str(['usrNew',newUsrName,newPass]).encode())
    username = input('USERNSME --> ')
    password = input('PASSWORD --> ')
    client_socket.send(str(['usrVal',username,password]).encode())
    # send message['usrVal',username,password]
    
    done = True
    isAdmin = False
    while done:
        data = client_socket.recv(1024).decode()
        if data:
            print('Received from server: ' + data)
            if data == 'userNOTValidated':
                quit('WRONG PASSWORD / WRONG USERNAME')
            if data == 'adminGranted':
                isAdmin = True
                print('[LOGIN] You are now a administrator')
            if data == 'adminNotGranted':
                print('[LOGIN] Wrong Password')

        try:
            inp = getch()
        except:pass

        if inp != None and inp != '$':
            inp_ = input('what to do? --> ')
            if inp_ == 'trans':
                address_ = input('to who? --> ')
                amount_ = input('amount to transfer --> ')
                client_socket.send(str(['trans',address_,amount_]).encode())
            if inp_ =='bal':
                client_socket.send(str(['bal',username]).encode())


        if inp == '$':
            if isAdmin:
                command = input('[COMMAND] --> ')
                command = '[' + command + ']'
                client_socket.send(command.encode())
            else:
                passw = input('[LOGIN] Admin password --> ')
                client_socket.send(str(['admLogin',passw]).encode())
    client_socket.close()

client_program()
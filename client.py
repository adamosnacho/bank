import socket
from getch import getche, getch
host = '192.168.0.63'
port = 6000  # socket server port number
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
    while done:
        data = client_socket.recv(1024).decode()
        if data:
            print('Received from server: ' + data)
            if data == 'userNOTValidated':
                quit('WRONG PASSWORD!')
        try:
            inp = getch()
            print(inp)
        except:pass
        if inp == 'command':
            command = input('[COMMAND] --> ')
            client_socket.send(str(command).encode())
    client_socket.close()

client_program()
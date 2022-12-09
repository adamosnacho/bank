import socket
from threading import Thread
from getch import getche, getch
quitMsg = 'quit'
host = '0.0.0.0'
port = 5000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server_socket = socket.socket()
server_socket.bind((host, port))
print(myip)
connected = False
done = False
server_socket.listen(1)  # accept new connection
while not done:
    if connected == False:
        conn, address = server_socket.accept()
        connected = True
    else:
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
            except:conn.send('done'.encode())
        if eval(data)[0] == 'trans':
            try:
                reciver = eval(data)[2]
                sender = eval(data)[1]
                amount = eval(data)[3]
                fsr = open(sender +'.txt','r')
                frr = open(reciver +'.txt','r')
                _s = eval(fsr.read())
                _r = eval(frr.read())
                _sa = eval(str(_s))[0]
                _ra = eval(str(_r))[0]
                fsr.close()
                frr.close()
                if float(_sa) < float(amount):
                    pass
                    
                else:
                    fsw = open(sender +'.txt','w')
                    frw = open(reciver +'.txt','w')
                    nsa = float(_sa) - float(amount)
                    nra = float(_ra) + float(amount)
                    _s[0] = nsa
                    _r[0] = nra
                    fsw.write(str(_s))
                    frw.write(str(_r))
                    fsw.close()
                    frw.close()
                conn.send('done'.encode())
            except:
                conn.send('Somthing is wrong...'.encode())
        if eval(data)[0] == 'setbal':
            fr = open(eval(data)[1]+'.txt','r')
            user = eval(fr.read())
            fr.close()
            user[0] = eval(data)[2]
            fw = open(eval(data)[1]+'.txt','w')
            fw.write(str(user))
            fw.close()
            conn.send('done'.encode())
        if eval(data)[0] == 'p':
            conn.send('p'.encode())
        if eval(data)[0] == 'disconnect':
            conn.close()
            connected = False
        if eval(data)[0] == 'stopServer':
            done = True
        if eval(data)[0] == '$':
            inp_ = input('-->')
            if inp_ == 'stop':
                done = True
            else:
                conn.send(inp_.encode())




        
conn.close()

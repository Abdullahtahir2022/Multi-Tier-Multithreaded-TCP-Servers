import socket
import random


Users = [("Abdullah","1234"),("Manzoor","6789")]
address = "127.0.0.1"
port = 5055

s = socket.socket()
s.bind((address,port))
s.listen(5)

def authenticate(username,password):
    print(username,password)
    for x in range(len(Users)):
        if(Users[x][0]==username and Users[x][1]==password):
            token = random.randint(0,100)
            return str(token)
    return False


while(True):
    c_s, addr = s.accept()
    print("Identity is active")
    username = c_s.recv(1024).decode("utf-8")
    password = c_s.recv(1024).decode("utf-8")
    print(username,password)
'''    Token = authenticate(username,password)
    c_s.send(Token.encode("utf-8"))'''
    
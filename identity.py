import socket
import random
import json


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
    return "False"


while(True):
    c_s, addr = s.accept()
    print("Identity is active")
    login_dump = c_s.recv(1024).decode("utf-8")
    login = json.loads(login_dump)
    print(login)
    Token = authenticate(login[0],login[1])
    c_s.send(Token.encode("utf-8"))
    
import socket
import json

address = "127.0.0.1"
port = 5051
au = []

s = socket.socket()
s.connect((address,port))

def get_funtionality(s):
    service = s.recv(1024).decode("utf-8")
    service = json.loads(service)
    for data in service:
        print(data)

def Enter_service_no(s,Token):
    service_number = input("Enter a corresponding number: ")
    s.send(service_number.encode("utf-8"))
    s.send(Token.encode("utf-8"))

def get_output(s):
    ip = s.recv(1024).decode("utf-8")
    port = s.recv(1024).decode("utf-8")
    j_port = json.loads(port)
    return ip,j_port

def authentication(s):
    username = input("Input Username: ")
    password = input("Input Password: ")
    au.append(username)
    au.append(password)
    login_dump = json.dumps(au)
    s.send(login_dump.encode("utf-8"))
    Token = s.recv(1024).decode("utf-8")
    return Token

def Connection_server(addr):
    s = socket.socket()
    s.connect((addr[0],addr[1]))
    return s

def Service(s,Token):
    string = input("Enter String: ")
    s.send(string.encode("utf-8"))
    s.send(Token.encode("utf-8"))




Token = authentication(s)
if(Token=="False"):
    print("Invalid Crendentials")
else:
    get_funtionality(s)
    Enter_service_no(s,Token)
    address = get_output(s)
    print(address)
    skt = Connection_server(address)
    Service(skt,Token)
    output = skt.recv(1024).decode("utf-8")
    print(output)
    
    




s.close()
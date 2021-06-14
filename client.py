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

def Enter_service(s):
    string = input("Enter a String: ")
    service_number = input("Enter a corresponding number: ")
    s.send(string.encode("utf-8"))
    s.send(service_number.encode("utf-8"))

def get_output(s):
    string = s.recv(1024).decode("utf-8")
    return string

def authentication(s):
    username = input("Input Username: ")
    password = input("Input Password: ")
    au.append(username)
    au.append(password)
    login_dump = json.dumps(au)
    s.send(login_dump.encode("utf-8"))
    Token = s.recv(1024).decode("utf-8")
    return Token




Token = authentication(s)
print(Token)
'''
get_funtionality(s)
Enter_service(s)
string = get_output(s)
print(string)'''


s.close()
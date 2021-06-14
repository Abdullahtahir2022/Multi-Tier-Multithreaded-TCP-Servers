from threading import Thread
import socket
import json


class Mythread(Thread):
    def __init__(self,c_s):
        Thread.__init__(self)
        self.c_s = c_s
        self.services = ["1. Echo","2. Palindrome", "3. Length"]
        self.Tokens = []

    def get_client_requirnment(self):
        string = self.c_s.recv(1024).decode("utf-8")
        service_number = self.c_s.recv(1024).decode("utf-8")

        return string,service_number
    def send_functionality(self):
        service = json.dumps(self.services)
        self.c_s.send(service.encode("utf-8"))

    def server_1(self,string):
        address = "127.0.0.1"
        port = 5052
        s = socket.socket()
        s.connect((address,port))
        s.send(string.encode("utf-8"))
        string = s.recv(1024).decode("utf-8")
        return string

    def server_2(self,string):
        address = "127.0.0.1"
        port = 5053
        s = socket.socket()
        s.connect((address,port))
        s.send(string.encode("utf-8"))
        string = s.recv(1024).decode("utf-8")
        return string

    def server_3(self,string):
        address = "127.0.0.1"
        port = 5054
        s = socket.socket()
        s.connect((address,port))
        s.send(string.encode("utf-8"))
        string = s.recv(1024).decode("utf-8")
        return string






        
    def authentication_Identity(self):
        username = self.c_s.recv(1024).decode("utf-8")
        password = self.c_s.recv(1024).decode("utf-8")
        address = "127.0.0.1"
        port = 5055
        s = socket.socket()
        s.connect((address,port))
        print(username,password)
        s.send(username.encode("utf-8"))
        s.send(password.encode("utf-8"))
        Token = s.recv(1024).decode("utf-8")
        return Token





    def run(self):
        Token = self.authentication_Identity()
        if Token!="False":
            self.Tokens.append(Token)
        self.c_s.send(Token.encode("utf-8"))




'''        self.send_functionality()
        values = self.get_client_requirnment()

        if(values[1]=="1"):
            string = self.server_1(values[0])
            self.c_s.send(string.encode("utf-8"))

        elif(values[1]=="2"):
            string = self.server_2(values[0])
            self.c_s.send(string.encode("utf-8"))
        elif(values[1]=="3"):
            string = self.server_3(values[0])
            self.c_s.send(string.encode("utf-8"))'''

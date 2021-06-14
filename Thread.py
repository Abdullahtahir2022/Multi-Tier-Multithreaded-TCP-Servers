from threading import Thread
import socket
import json


class Mythread(Thread):
    def __init__(self,c_s):
        Thread.__init__(self)
        self.c_s = c_s
        self.services = ["1. Echo","2. Palindrome", "3. Length"]
        self.Tokens = []
        self.Token_status = False

    def get_client_requirnment(self):
        string = self.c_s.recv(1024).decode("utf-8")
        service_number = self.c_s.recv(1024).decode("utf-8")
        Token = self.c_s.recv(1024).decode("utf-8")

        return string,service_number,Token
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
        login = self.c_s.recv(1024).decode("utf-8")
        address = "127.0.0.1"
        port = 5055
        s = socket.socket()
        s.connect((address,port))
        s.send(login.encode("utf-8"))
        Token = s.recv(1024).decode("utf-8")
        return Token


    def Token_Validation(self, values):

        for tkn in self.Tokens:
            if tkn == values[2]:
                self.Token_status = True
            else:
                self.Token_status = False




    def run(self):
        Token = self.authentication_Identity()
        if Token!="False":
            self.Tokens.append(Token)
        self.c_s.send(Token.encode("utf-8"))

        self.send_functionality()
        values = self.get_client_requirnment()
        self.Token_Validation(values)



        if self.Token_status == True:
            if(values[1]=="1"):
                #string = self.server_1(values[0])
                ip = "127.0.0.1"
                port = 5052
                j_port = json.dumps(port)
                self.c_s.send(ip.encode("utf-8"))
                self.c_s.send(j_port.encode("utf-8"))
            elif(values[1]=="2"):
                ip = "127.0.0.1"
                port = 5053
                j_port = json.dumps(port)
                self.c_s.send(ip.encode("utf-8"))
                self.c_s.send(j_port.encode("utf-8"))
            elif(values[1]=="3"):
                ip = "127.0.0.1"
                port = 5054
                j_port = json.dumps(port)
                self.c_s.send(ip.encode("utf-8"))
                self.c_s.send(j_port.encode("utf-8"))

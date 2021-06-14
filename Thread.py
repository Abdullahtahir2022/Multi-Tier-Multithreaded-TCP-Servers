from threading import Thread
import socket
import json



class Mythread(Thread):
    def __init__(self,c_s,Tokens):
        Thread.__init__(self)
        self.c_s = c_s
        self.Tokens = Tokens
        self.services = ["1. Echo","2. Palindrome", "3. Length"]
        self.Token_status = False

    def get_client_requirnment(self):
        service_number = self.c_s.recv(1024).decode("utf-8")
        Token = self.c_s.recv(1024).decode("utf-8")

        return service_number,Token
    def send_functionality(self):
        service = json.dumps(self.services)
        self.c_s.send(service.encode("utf-8"))



        
    def authentication_Identity(self,login):
        address = "127.0.0.1"
        port = 5055
        s = socket.socket()
        s.connect((address,port))
        s.send(login.encode("utf-8"))
        Token = s.recv(1024).decode("utf-8")
        return Token


    def Token_Validation(self, values):

        for tkn in self.Tokens:
            if tkn == values:
                self.Token_status = True
                break
            else:
                self.Token_status = False

    def Server_1(self):
        ip = "127.0.0.1"
        port = 5052
        j_port = json.dumps(port)
        self.c_s.send(ip.encode("utf-8"))
        self.c_s.send(j_port.encode("utf-8"))

    def Server_2(self):
        ip = "127.0.0.1"
        port = 5053
        j_port = json.dumps(port)
        self.c_s.send(ip.encode("utf-8"))
        self.c_s.send(j_port.encode("utf-8"))

    def Server_3(self):
        ip = "127.0.0.1"
        port = 5054
        j_port = json.dumps(port)
        self.c_s.send(ip.encode("utf-8"))
        self.c_s.send(j_port.encode("utf-8"))




    def run(self):
        output = self.c_s.recv(1024).decode("utf-8")
        if output == "validation":
            self.c_s.send("ok".encode("utf-8"))
            Token = self.c_s.recv(1024).decode("utf-8")
            self.Token_Validation(Token)
            if self.Token_status == True:
                self.Tokens.remove(Token)
                self.c_s.send("True".encode("utf-8"))
            else:
                self.c_s.send("False".encode("utf-8"))


        else:
            Token = self.authentication_Identity(output)
            if Token!="False":
                self.Tokens.append(Token)
            self.c_s.send(Token.encode("utf-8"))
            self.send_functionality()
            values = self.get_client_requirnment()
            self.Token_Validation(values[1])
            if self.Token_status == True:
                if(values[0]=="1"):
                    self.Server_1()
                elif(values[0]=="2"):
                    self.Server_2()
                elif(values[0]=="3"):
                    self.Server_3()

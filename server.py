import socket
from Thread import Mythread
import json

address = "127.0.0.1"
port = 5051
Tokens = []

s = socket.socket()
s.bind((address,port))
s.listen(5)


    



while(True):
    print("Main server is Active")
    c_s, addr = s.accept()
    client_thread = Mythread(c_s,Tokens)
    client_thread.start()








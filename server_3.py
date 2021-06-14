import socket


address = "127.0.0.1"
port = 5054

s = socket.socket()
s.bind((address,port))
s.listen(5)

while(True):
    c_s, addr = s.accept()
    print("Server_3 is active")
    string = c_s.recv(1024).decode("utf-8")
    length = str(len(string))
    c_s.send(length.encode("utf-8"))
    print("server_3 here")
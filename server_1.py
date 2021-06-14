import socket



address = "127.0.0.1"
port = 5052

s = socket.socket()
s.bind((address,port))
s.listen(5)

while(True):
    c_s, addr = s.accept()
    print("Server_1 is active")
    string = c_s.recv(1024).decode("utf-8")
    c_s.send(string.encode("utf-8"))
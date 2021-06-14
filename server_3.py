import socket


address = "127.0.0.1"
port = 5054

s = socket.socket()
s.bind((address,port))
s.listen(5)

def Main_server(Token):
    address = "127.0.0.1"
    port = 5051
    s = socket.socket()
    s.connect((address,port))
    s.send("validation".encode("utf-8"))
    output = s.recv(1024).decode("utf-8")
    print(output)
    if output == "ok":
        s.send(Token.encode("utf-8"))
    validation = s.recv(1024).decode("utf-8")
    return validation


while(True):
    c_s, addr = s.accept()
    print("Server_3 is active")
    string = c_s.recv(1024).decode("utf-8")
    Token = c_s.recv(1024).decode("utf-8")
    validation = Main_server(Token)    
    length = str(len(string))
    if validation == "True":
        c_s.send(length.encode("utf-8"))
    else:
        c_s.send("Invalid User".encode("utf-8"))

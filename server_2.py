import socket


address = "127.0.0.1"
port = 5053

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

def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


while(True):
    c_s, addr = s.accept()
    print("Server_2 is active")
    string = c_s.recv(1024).decode("utf-8")
    Token = c_s.recv(1024).decode("utf-8")
    validation = Main_server(Token)    
    res = isPalindrome(string)
    if res == True and validation == "True":
        c_s.send("True".encode("utf-8"))
    else:
        c_s.send("False".encode("utf-8"))
    
    print("server_2 here")


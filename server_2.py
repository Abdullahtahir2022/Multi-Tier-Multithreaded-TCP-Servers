import socket


address = "127.0.0.1"
port = 5053

s = socket.socket()
s.bind((address,port))
s.listen(5)

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
    res = isPalindrome(string)
    if(res):
        c_s.send("True".encode("utf-8"))
    else:
        c_s.send("False".encode("utf-8"))
    
    print("server_2 here")


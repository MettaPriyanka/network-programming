#first of all import the socket library
import socket

#next create a socket object
s = socket.socket()
print("Soxket Successfully Created")

#reserve a port on your computer in our
#case it 40674 but it can be anything
port = 40674

#next  bind to port#we have not typed any ip in the ip field
#instead we having the inputed an empty string
#this makes the server listen to requests
#coming from yhe computers on the network
s.bind(('', port))
print("socket binded to %s"%(port))
s.listen(5)
print("socket is listening")
while True:
    #establish connection with client
    c,addr = s.accept()
    print('Got connection from',addr)
    c.send(b'Thank you dor connecting')
    c.close()
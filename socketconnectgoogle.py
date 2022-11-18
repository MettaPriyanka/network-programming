import socket
import sys
try:
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Successfully created")
except socket.error as err:
    print("socket creation failed with error %s"%(err))
port = 80

try:
    host_ip = socket.gethostbyname('www.google123.com')
except socket.gaierror:
        
    print("there was an error resolving the host")
    sys.exit()
    
s.connect((host_ip,port))
print(host_ip)
print("the socket has successfuly connected to google")

import socket
hostname= socket.gethostname()
ipadd = (socket.gethostbyname(hostname))
print(hostname)
print(ipadd)
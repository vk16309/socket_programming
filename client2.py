import socket
c=socket.socket()
c.connect(('localhost',9999))
print("Connection established")
message=input("Enter your message")
destination=input("Enter destination address")
c.send(bytes({"message":message,"destination":destination}),"utf-8")
print("message sent")
while True:
    recieved=c.recv(1024).decode()
    if recieved:
        print(recieved)
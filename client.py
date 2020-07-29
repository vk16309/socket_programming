import socket
import json

c=socket.socket()
c.connect(('localhost',9999))
print("Connection established")
message=input("Enter your message")
destination=input("Enter destination address")
data=json.dumps({"message":message,"destination":destination}).encode('utf-8')
c.send(data)
print("message sent")
while True:
    recieved=c.recv(1024).decode()
    if recieved:
        print(recieved)
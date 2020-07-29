import socket
import json

s=socket.socket()
s.bind(('localhost',9999))
s.listen(7)
print("listening for request")
connected=dict()
while True:
    c,addr=s.accept()
    connected[str(addr[1])]=c
    print("connected with",addr)
    while True:
        recieved=json.loads(c.recv(1024).decode())
        print(recieved)
        if recieved:
            print(recieved)
            print(connected)
            if recieved['destination'] in connected.keys():
                dest=connected[recieved['destination']]
                dest.send(bytes(recieved['message'],'utf-8'))
                print("Message Sent")
            else:
                print("Destination device not connected")


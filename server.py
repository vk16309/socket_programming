import socket
import json

s=socket.socket()
s.bind(('localhost',9999))
s.listen(3)
print("listening for request")
connected=dict()
while True:
    try:
        s.settimeout(3)
        c,addr=s.accept()
        c.send(bytes(str(addr[1]),'utf-8'))
        connected[str(addr[1])]=c
        print("connected with",addr)
        print(connected)
    except Exception as e:
        print(">>>>")
    for sender,c in connected.items():
        try:
            c.settimeout(0.5)
            recieved=json.loads(c.recv(1024).decode())
            print(recieved)
            if recieved:
                print(recieved)
                print(connected)
                if recieved['destination'] in connected.keys():
                    dest=connected[recieved['destination']]
                    dest.send(bytes(recieved['message']+" --> from: "+sender,'utf-8'))
                    print("Message Sent")
                else:
                    print("Destination device not connected")
        except Exception as e:
            print("...")


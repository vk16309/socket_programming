import socket
import json

c=socket.socket()
c.connect(('localhost',9999))
print("Assigned port number:",c.recv(1024).decode())
print("Connection established")

while True:
    choice=input("Enter check or send:  ")
    if choice.lower()=="send":
        message = input("Enter your message:  ")
        destination = input("Enter destination address:  ")
        data = json.dumps({"message": message, "destination": destination}).encode('utf-8')
        c.send(data)
        print("\nmessage sent\n\n")
    elif choice.lower()=="check":
            try:
                c.settimeout(2.0)
                recieved = c.recv(1024)
                print(len(recieved))
                recieved=recieved.decode()
                if recieved:
                    print("Message: ",recieved,"\n\n")
            except Exception as e:
                print("No new messages there!\n\n")
                pass

    else:
        print("Wrong choice\n")

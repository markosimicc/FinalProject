import json
import socket, sys, time
import final
"""
Author: Marko Simic
This code is used on the Server Rpi connected via ethernet to the Client RPi
Operating on ip 192.168.1.10
REcieves and Sends informtion from direct acces to the database
"""

"""
functionality is used to determine what do to wwith the function recieved
input: String funct
"""
def functionality(funct):
    if(funct == 'decrease'):
        amount = message['amount']
        flag = final.decreaseQuantity(i,amount)
        SendACK(mid,flag)#sends acknowlegment to Cleint
    elif(funct == 'increase'):
            amount = message['amount']
            flag = final.increaseQuantity(i,amount)
            SendACK(mid,flag)#sends acknowlegment to Client
    elif(funct == 'getPrice'):
        price = final.getPrice(i)
        SendInfo(mid,price)#sends Info to Client
    elif(funct == 'getQuantity'):
        quantity = final.getQuantity(i)
        SendInfo(mid,quantity)#sends Info to Client
    elif(funct == 'getItem'):
         item = final.getItem(i)
         SendInfo(mid,item)#sends Info to Client
    elif(funct == 'getName'):
        name = final.getName(i)
        SendInfo(mid,name)#sends Info to Client
    else:
        return False
"""
sendACK sends an ackwowledgement of when function is completed back to the Client
Inputs: int mid, boolean flag
the messagenumber received and the flag of whether the function was completed or not
"""
def SendACK(mid,flag):
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)#ip of client
    reply = {"messagenum":mid,"complete": flag}#dictionary of values
    data = json.dumps(reply).strip()#send JSON
    so.sendto(data.encode('utf-8'),server_address1)
    #print(data)
"""
sendInfo sends Info of the requested data back to the client
Inputs: int mid, string info
the messagenumber received and the info that he client requested
eitehr the name or price of the item
"""
def SendInfo(mid,info):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address2 = ('192.168.1.20',5053)#ip of client
    reply = {"messagenum":mid,"info": info}#dictionary of values
    data = json.dumps(reply).strip()
    soc.sendto(data.encode('utf-8'),server_address2)
    #print(data)
#always running
while(1):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.1.10',5051)#recieving in this port
    s.bind(server_address)
    buf, address = s.recvfrom(5051)
    message = json.loads(buf.decode('utf-8'))#decode data recieved
    #print(message)
    function = message["func"]
    mid = message["messagenum"]
    i = message["id"]
    functionality(function)#find functionality of function recieved
  

import json
import socket, sys, time
import final
def functionality(funct):
    if(funct == 'decrease'):
        amount = message['amount']
        flag = final.decreaseQuantity(i,amount)
        SendACK(mid,flag)
    elif(funct == 'increase'):
            amount = message['amount']
            flag = final.increaseQuantity(i,amount)
            SendACK(mid,flag)
    elif(funct == 'getPrice'):
        price = final.getPrice(i)
        SendInfo(mid,price)
    elif(funct == 'getQuantity'):
        quantity = final.getQuantity(i)
        SendInfo(mid,quantity)
    elif(funct == 'getItem'):
         item = final.getItem(i)
         SendInfo(mid,item)
    elif(funct == 'getName'):
        name = final.getName(i)
        SendInfo(mid,name)
    else:
        return False

def SendACK(mid,flag):
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)
    reply = {"messagenum":mid,"complete": flag}
    data = json.dumps(reply).strip()
    so.sendto(data.encode('utf-8'),server_address1)
    print(data)

def SendInfo(mid,info):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address2 = ('192.168.1.20',5053)
    reply = {"messagenum":mid,"info": info}
    data = json.dumps(reply).strip()
    soc.sendto(data.encode('utf-8'),server_address2)
    print(data)
while(1):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    port = int(textport)
    server_address = ('192.168.1.10',5051)
    s.bind(server_address)
    buf, address = s.recvfrom(5051)
    message = json.loads(buf.decode('utf-8'))
    print(message)
    function = message["func"]
    mid = message["messagenum"]
    i = message["id"]
    functionality(function)
  

import json
import socket, sys, time
import final
textport = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('192.168.1.10',port)
s.bind(server_address)
buf, address = s.recvfrom(port)
message = json.loads(buf.decode('utf-8'))
print(message)
function = message["func"]
mid = message["messagenum"]
i = message["id"]
def functionality(funct):
    if(funct == 'decrease'):
        amount = message['amount']
        return final.decreaseQuantity(i,amount)
    elif(funct == 'increase'):
            amount = message['amount']
            return final.increaseQuantity(i,amount)
    elif(funct == 'getPrice'):
        return final.getPrice(i)
    elif(funct == 'getQuantity'):
        return final.getQuantity(i)
    elif(funct == 'getItem'):
        return final.getItem(i)
    else:
        return False

def SendACK(mid,flag):
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)
    reply = {"messagenum":mid,"complete": flag}
    data = json.dumps(reply).strip()
    so.sendto(data.encode('utf-8'),server_address1)
    print(data)

flag = functionality(function)
SendACK(mid,flag)

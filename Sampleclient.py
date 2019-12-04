import serial
import socket,sys,time
import json
arduino = serial.Serial('/dev/ttyACM0',9600)
previousIndex = 100
data = {
    'messagenum' : 0,
    'id' : 1,
    'func' : None,
    'amount' : None
}
def recACK():
    s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)
    s2.bind(server_address1)
    buf, address = s2.recvfrom(5053)
    message = json.loads(buf.decode('utf-8'))
    print(message)
def recINFO():
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)
    soc.bind(server_address1)
    buf, address = soc.recvfrom(5053)
    message = json.loads(buf.decode('utf-8'))
    data = message["info"]
    data = (str)(data)
    print(data)
    arduino.write(data)
    print(message)
def incrementMessageNum(count):
    if(count < 1000):
        count += 1
        return count
    else:
        return 1
messageCount = 1
while(1):
    senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.1.10', 5051)
    incomingData = arduino.readline()
    numData = (int)(incomingData)
    print(incomingData)
    if((numData > previousIndex) and (numData <=100)):
        change = numData - previousIndex
        previousIndex = previousIndex + change
        data["messagenum"] = messageCount
        data["func"] = 'increase'
        data["amount"] = change
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        print(send)
        recACK()
        messageCount = incrementMessageNum(messageCount)
    elif((numData < previousIndex) and (numData >= 0)):
        change = previousIndex -  numData
        previousIndex = previousIndex - change
        data["messagenum"] = messageCount
        data["func"] = 'decrease'
        data["amount"] = change
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        print (send)
        recACK()
        messageCount = incrementMessageNum(messageCount)
    elif(numData == 1001):
        data["messagenum"] = messageCount
        data["func"] = 'getName'
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        print(send)
        recINFO()
        messageCount = incrementMessageNum(messageCount)
    elif(numData == 1002):
        data["messagenum"] = messageCount
        data["func"] = 'getPrice'
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        print(send)
        recINFO()
        messageCount = incrementMessageNum(messageCount)
    elif(numData == previousIndex):
        print("no change")
    else:
        print("The arduino is malfunctioning")
    
    

    
    
   
   

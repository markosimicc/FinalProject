import serial
import socket,sys,time
import json
"""
Author: Marko Simic
This code below is used to be run on the Client Raspberry Pi
Arduino Uno with uploaded code is connected through wired UDP.
Client Raspberry Pi is running with ethernet connection to Server RPi
Client RPi is operating on IP address 192.168.1.20
"""
#Arduino is plugged into Serial Port and client can read and write from Serial
arduino = serial.Serial('/dev/ttyACM0',9600)
previousIndex = 100 # Quantity of shelf starts full
# Message format for JSON to be sent
data = {
    'messagenum' : 0,
    'id' : 1,
    'func' : None,
    'amount' : None
}
"""
recACK is a function which receieves a JSON message from the Server
It recieves a JSON message to comfirm that it was recieved and
whetehr it was complete or not, the ystem is only making sure that the message was recieved
if the message could be processed teh system continues operating
"""
def recACK():
    s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)#Ethernet IP address and port 5053
    s2.bind(server_address1)
    buf, address = s2.recvfrom(5053)
    message = json.loads(buf.decode('utf-8'))
    #print(message) - prints the message used for testing
"""
recInfo is used to recieve info from the Server
The info being the Price or name
Th einfo is displayed on the LCD
"""
def recINFO():
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address1 = ('192.168.1.20',5053)#receieves info
    soc.bind(server_address1)
    buf, address = soc.recvfrom(5053)
    message = json.loads(buf.decode('utf-8'))#load json
    data = message["info"]#data needed
    data = (str)(data)#make it a string
    #print(data)
    arduino.write(data)#write the data to the arduino for use
    #print(message)
"""
incrementMessageNum i scalled to increment the messagenum for the messages being sent
messagenum is rest to 1 after 1000 messages to ensure that when the system is running
for a long time it isnt sending very large message numbers
"""
def incrementMessageNum(count):
    if(count < 1000):
        count += 1
        return count
    else:
        return 1
messageCount = 1#messagenum begins at 1
#The below code is always running hence the while loop
while(1):
    senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.1.10', 5051)#sends to server on 192.168.10 on port 5051
    incomingData = arduino.readline()##reads info given from arduino
    numData = (int)(incomingData)#cast as an int
    #print(incomingData)
    """
If the number is greater than the previous index and is less than 100
the system got an increase in the quantity
The JSON dcitionary data is updated to send the info
"""
    if((numData > previousIndex) and (numData <=100)):
        change = numData - previousIndex#calculates change
        previousIndex = previousIndex + change#updates previous index
        data["messagenum"] = messageCount
        data["func"] = 'increase'
        data["amount"] = change
        send = json.dumps(data)#dump data tp JSON format
        senderSocket.sendto(send.encode('utf-8'),server_address)
        #print(send)
        recACK()#calls to reciev acknowlegdement from server
        messageCount = incrementMessageNum(messageCount)#increment mesagenum
          """
If the number is less than the previous index and is more than 0
the system got an decrease in the quantity
The JSON dcitionary data is updated to send the info
"""
    elif((numData < previousIndex) and (numData >= 0)):
        change = previousIndex -  numData#change ijn qunatity
        previousIndex = previousIndex - change#update previous index
        data["messagenum"] = messageCount
        data["func"] = 'decrease'
        data["amount"] = change
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        #print (send)
        recACK()#go to recieve ack after sending message
        messageCount = incrementMessageNum(messageCount)#increment mesagenum
        """
if the number read is 1001 the arduino is requesting the name of the item
must recieve info from the server
"""
    elif(numData == 1001):
        data["messagenum"] = messageCount
        data["func"] = 'getName'
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        #print(send)
        recINFO()#must go to recieve info from server
        messageCount = incrementMessageNum(messageCount)#increment mesagenum
        """
if the number read is 1002 the arduino is requesting the price of the item
must recieve info from the server
"""
    elif(numData == 1002):
        data["messagenum"] = messageCount
        data["func"] = 'getPrice'
        send = json.dumps(data)
        senderSocket.sendto(send.encode('utf-8'),server_address)
        #print(send)
        recINFO()#miust go to recieve info from server
        messageCount = incrementMessageNum(messageCount)#increment mesagenum
    elif(numData == previousIndex):
        print("no change")#no change inthe system quantity
    else:
        print("The arduino is malfunctioning")#error in the arduino mesages being sent
    
    

    
    
   
   

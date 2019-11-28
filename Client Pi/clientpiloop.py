import serial, time, sys, socket, json

serPort = serial.Serial('/dev/ttyACM0',9600)

previousIndex = 0

host = sys.argv[1]
textport = sys.argv[2]


data = {
	'messagenum' : 0,
	'id' : 0,
	'func' : None
	'amount' : None
}

messageCount = 0

senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

def remove_chars(stringValue):
	stringList = list(stringValue)
	stringList.remove('\\')
	stringList.remove('r')
	stringList.remove('n')
	return ''.join(stringList)

def incrementMessageNum(count):
	if(count < 1000):
		count += 1
		return count
	else:
		return 1


while(1):
	incomingID = None
	incomingID = serPort.readline()
	incomingID = remove_chars(incomingID)

	incomingData = None
	incomingData = serPort.readline()
	incomingData = remove_chars(incomingData)
	try:
		incomingData = (int)(incomingData)
	except:
		print("Error Occured: Incoming Data is not integer value")

	if((incomingData >= 0) && (incomingData <= 100)):
		totalChange = incomingData - previousIndex
		if( totalChange < 0):
			data[messagenum] = messageCount
			data['id'] = incomingID
			data[func] = "decrease"
			data[amount] = (str)(totalChange)
		elif (totalChange > 0):
			data[messagenum] = messageCount
			data['id'] = incomingID
			data[func] = "increase"
			data[amount] = (str)(totalChange)

		data = json.dumps(data)
		senderSocket.sendto(data.encode('utf-8'), server_address)

	elif(incomingData == 1001):
		data[messagenum] = messageCount
		data['id'] = incomingID
		data['func'] = "getName"
		data['data'] = ''

		data = json.dumps(data)
		senderSocket.sendto(data.encode('utf-8'), server_address)

	elif(incomingData == 1002):
		data[messagenum] = messageCount
		data['id'] = incomingID
		data['func'] = "getName"
		data['data'] = ''

		data = json.dumps(data)
		senderSocket.sendto(data.encode('utf-8'), server_address)

	else:
		print("Index out of range")

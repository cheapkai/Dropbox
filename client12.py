import os
import time
from socket import *
serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1',serverPort))
sentence = raw_input('Enter command:')

commands = sentence.split(' ')

clientSocket.send(sentence)
strb = "/home/mehthab/SOSC/history"

with open(strb, 'a+') as foo:
	foo.write("\n")
	foo.write(sentence)
	strd = time.ctime(os.path.getmtime("/home/mehthab/SOSC/history")).split(" ")[3]
	foo.write(" "+ "time :" + strd)

foo.close()


modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

if  commands[1] == "TCP" :

	clientSocket2 = socket(AF_INET, SOCK_STREAM)
	clientSocket2.connect(('127.0.0.1',12345))
	filename = commands[2]
	strn = "/home/mehthab/SOSC/" + str(filename)

	with open(strn, 'wb') as f:
		while True:
			data = clientSocket2.recv(1024)
			if not data:
				break

			f.write(data)
	f.close()

	clientSocket2.close()

if commands[1] == "UDP" :

	filename = commands[2]

	#clientSocket2 = socket
	clientSocket3 = socket(AF_INET, SOCK_DGRAM)
	message = "Send"


	clientSocket3.sendto(message,('127.0.0.1',12344))
	modifiedMessage, serverAddress = clientSocket3.recvfrom(2048)

	print modifiedMessage

	strn = "/home/mehthab/SOSC/" + str(filename)
	ffl = 1

	with open(strn,'wb') as f:
		while True:
			print 'a'

			#D = clientSocket.recv(1024)

			D , addr = clientSocket3.recvfrom(1024)

			if str(D) == "off":
				break

			clientSocket3.settimeout(30)	

			data, serverAddr = clientSocket3.recvfrom(1024)
			
			#if str(data) == "END" 



			if not data:
				print 'b'
				ffl = 0
			else :
				print 'c'


			#print (repr(data))	

			f.write(data)
			
	f.close()			
	#buf = 1024

	#f = open(strn,'wb')
	#data,addr = clientSocket3.recvfrom(buf)
	#try:
	#	while(data):
	#		f.write(data)
	#		clientSocket3.setdefaulttimeout(30)

	#		data,addr = clientSocket3.recvfrom(buf)

	#except timeout:
	#	f.close()
	#	clientSocket3.close()

	#print "File Downloaded"




	clientSocket3.close()










clientSocket.close()

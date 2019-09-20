import os
import time
import hashlib
from socket import *
serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1',serverPort))
sentence = raw_input('Enter command:')

commands = sentence.split(' ')

#clientSocket.send(sentence)
strb = "/home/mehthab/SOSC/history"

with open(strb, 'a+') as foo:
	foo.write("\n")
	foo.write(sentence)
	strd = time.ctime(os.path.getmtime("/home/mehthab/SOSC/history")).split(" ")[3]
	foo.write(" "+ "time :" + strd)

foo.close()



if commands[0] == "FileDownload":
	tog = 1

	while tog:
		clientSocket.send(sentence)

		modifiedSentence = clientSocket.recv(1024)
		print 'From Server:', modifiedSentence
		checker = modifiedSentence.split(" ")
		nik = len(checker)
		chk = checker[nik - 1]

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
			clientSocket3 = socket(AF_INET, SOCK_DGRAM)
			message = "Send"
			clientSocket3.sendto(message,('127.0.0.1',12344))
			modifiedMessage, serverAddress = clientSocket3.recvfrom(2048)
			print modifiedMessage
			strn = "/home/mehthab/SOSC/" + str(filename)
			ffl = 1
			with open(strn,'wb') as f:
				while True:
					#print 'a'
					D , addr = clientSocket3.recvfrom(1024)
					if str(D) == "off":
						break
					clientSocket3.settimeout(30)	
					data, serverAddr = clientSocket3.recvfrom(1024)
					if not data:
					#	print 'b'
						ffl = 0
					else :
						kk = 90
					#	print 'c'

					f.write(data)

			f.close()			
			clientSocket3.close()
			
		hasher = hashlib.md5()
		with open(strn  , 'rb') as afile:
			buf = afile.read()
			hasher.update(buf)
			checksum = hasher.hexdigest()
 		
 		print chk
 		print checksum
 		if checksum in chk:
 			tog = 0
 			print 'File Download Complete'

 	
 	#clientSocket.close()
		






else :
	clientSocket.send(sentence)




	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence

	#clientSocket.close()


clientSocket.close()



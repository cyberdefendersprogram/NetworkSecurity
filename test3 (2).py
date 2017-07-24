import socket
import os

URL = raw_input("Would you like to look out for a certain URL: ")

if URL:	
	try:
		Inverse = socket.gethostbyname(URL)
		Reverse = socket.gethostbyaddr(Inverse)[2]
	except socket.gaierror:
		print("Incorrect URL, please try again")
		os.system('python test3.py')
if not URL:
	Reverse = "nothing"


if Reverse:
	try:
		while True:
			from pygame import *	
			import time	
			import os
			import sys

			#host = input("This is a test: ")
			#print(host)
		
		
		
			os.system('tshark -a duration:30 -T psml > TEST123.txt')
		
			from collections import Counter

			datain = open("TEST123.txt")
			dataout = open("Test2.txt", "w+")

			delete_list = ['<packet>','<section>','</section>','<structure>','</packet>','</structure>']
			for line in datain:
			    for word in delete_list:
				line = line.replace(word, "")
			    dataout.write(line)
			datain.close()
			dataout.close()

			f = open("Test2.txt","r")

			class Packet(object):
			    def __init__(name, number, time, source, destination, protocal, length, info): #Constructor for all of the information
				name.number = number
				name.time = time
				name.source = source
				name.destination = destination
				name.protocal = protocal
				name.length = length
				name.info = info

			    def displayInfo(self): #Method for displaying the data
				print("Number : ", self.number,
				      "Time : ", self.time,
				      "Source : ", self.source,
				      "Destination : ", self.destination,
				      "Protocal : ", self.protocal ,
				      "Length : " , self.length,
				      "Info : ", self.info)

			lines = f.readlines() #Variable set to read a certain line. ex: lines[1] will read the first line of the text file

			data = []
			destIp = []
			count = []

			for i in range(int(lines[-10])): #This for loop will repeat from 0 to the number that is located at the 5th to last line of the text file, which happens to be last packet number

				Number = lines[10*(i+1)+3] #Lines where the number is located
				Time = lines[10*(i+1)+4] #Lines where the time in seconds is located
				Source = lines[10 * (i + 1) + 5] #Lines where the source IP is located
				Destination = lines[10 * (i + 1) + 6] #Lines where the Destination IP is located
				Protocal = lines[10 * (i + 1) + 7] #Lines where the Protocal is located
				Length = lines[10 * (i + 1) + 8] #Lines where the Length is located
				Info = lines[10 * (i + 1) + 9] #Lines where the Info is located

				data.append([Number[0:len(Number) - 1],
					Time[0:len(Time) - 1],
					Source[0:len(Source) - 1],
					Destination[0:len(Destination) - 1],
					Protocal[0:len(Protocal) - 1],
					Length[0:len(Length) - 1],
					Info[0:len(Info) - 1]])

			    	#print(data[i][0:6])
				
				
			    	
			    	try:
					test1 = socket.gethostbyaddr(data[i][3])
			
					#test2 = socket.gethostbyname("google-public-dns-a.google.com")
			
					print(test1[2])
					print Reverse
						# print("DNS: ",test2)
					if test1[2] == Reverse[2]:
						mixer.init()
						mixer.music.load('ALARM')
						mixer.music.play()
						sys.exit()

										
					"""if Reverse[2] in socket.gethostbyaddr(data[i][3])[2]:
						mixer.init()
						mixer.music.load('ALARM')
						mixer.music.play()
						sys.exit()"""			
	
				except:
					pass

				if Destination[0].isalpha():
					destIp.append("0")
			    	else:
					destIp.append(Destination)
				# creating a counter
			
			
			
			
			counterList = Counter(destIp)
			mostOccuring = Counter(destIp).most_common(1)[0][1]
			print(counterList)
			print(mostOccuring)
		
		
		
			 #print(destIp)
		
			#if mostOccuring > 100:			
			#	mixer.init()
			#	mixer.music.load('ALARM')
			#	mixer.music.play()
		
			import smtplib

			server = smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login("cyberdefense1a2b3c@gmail.com","cyberdefense")
		
			msg = "\nMost Occuring IPs: %s - %d"%(counterList[0],mostOccuring)
		
			#server.sendmail("cyberdefense1a2b3c@gmail.com","silvachristian98@gmail.com",msg)
			#server.sendmail("cyberdefense1a2b3c@gmail.com","arturo.perez408@gmail.com",msg)
			server.quit()
			#print("google has been accessed this amount of times: ", Counter(count).most_common(1)[0][1])
			print("If you wish to stop, press Ctrl+C. Otherwise, wait 10 seconds to continue")
			time.sleep(10)
	except KeyboardInterrupt:
		pass


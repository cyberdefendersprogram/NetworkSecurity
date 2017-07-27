import socket
import os
import smtplib
import datetime
from email.mime.multipart import *
from email.mime.text import *
from email.mime.image import *
from email import encoders


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("cyberdefense1a2b3c@gmail.com","cyberdefense")


URL = input("Would you like to look out for a certain URL: ")#Input command for Reverse DNS. it can be any url


EMAIL = input("Please insert an email to begin: ")

if EMAIL:
	try:
		msg = "\nThank you, please wait as we prepare for packet scanning..."
		server.sendmail("cyberdefense1a2b3c@gmail.com",EMAIL,msg)
	except:
		msg = "\nEmail does not exist, please try again"
		os.system('python3 test3.py')

if URL:	
	try: #if the URL string has something, it will be checked
		Inverse = socket.gethostbyname(URL)
		Reverse = socket.gethostbyaddr(Inverse)[2]#these 2 lines will convert the url into a list that has the url and the ip that we need.
	except : #if the url doesn't work, the program will restart.
		print("Incorrect URL, please try again")
		os.system('python3 test3.py')
if not URL: #if you choose not to have a url, it will be filled for you.
		print("Incorrect URL, please try again")
		os.system('python3 test3.py')


if Reverse:
	currenttime = datetime.datetime.now().time()
	try: #this try statement will make the program run forever until you press Ctrl-C at the end
		URLcounter = 0
		datacount = open("TestURL.txt", "w")
		while True:
			from pygame import *	
			import time	
			import os
			import sys

		
	
	
	
			os.system('tshark -a duration:30 -T psml > TEST123.txt')#this will start tshark with a terminal command
	
			from collections import Counter #will count the highest used packet

			datain = open("TEST123.txt","r") 
			dataout = open("Test2.txt", "w")#these 2 lines will import and export packet data into a more readable format

			delete_list = ['<packet>','<section>','</section>','<structure>','</packet>','</structure>']
			for line in datain:
				for word in delete_list:
					line = line.replace(word,"")
				dataout.write(line)
			datain.close()
			dataout.close()

			f = open("Test2.txt","r")

			"""class Packet(object):
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
				      "Info : ", self.info)"""

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
				
				
				print("No.",data[i][0],
				"\nTime:\t\t",data[i][1],
				"\nSource:\t\t",data[i][2],
				"\nDestination:\t",data[i][3],
				"\nProtocal:\t",data[i][4],
				"\nLength:\t\t",data[i][5],
				"\nInfo:\t\t",data[i][6],
				"\n")
			
			
			    	
				try:
		
					
					print("----------------------------------------------------")
					
					
					if data[i][3] in Reverse:	
						URLcounter += 1
						datacount.writelines("\nNo."+data[i][0]+
				"\nTime:\t\t"+data[i][1]+
				"\nSource:\t\t"+data[i][2]+
				"\nDestination:\t"+data[i][3]+
				"\nProtocal:\t"+data[i][4]+
				"\nLength:\t\t"+data[i][5]+
				"\nInfo:\t\t"+data[i][6]+
				"\n"+
				"\r\n")
						
						

											
				except:
					print("----------------------------------------------------")				
					pass
			

				if Destination[0].isalpha():
					destIp.append("Broadcast")
				else:
					destIp.append(Destination)
				# creating a counter
		
		
		
		
			counterList = Counter(destIp)
			mostOccuring = Counter(destIp).most_common(1)[0][1]
			print("The most common IP",destIp[0])
			print("How many packets:",mostOccuring)
			print("The URL counter is: ", URLcounter)
	
				
			if mostOccuring > 10:
				for i in range (3):
					mixer.init()
					mixer.music.load('ALARM3.mp3')
					mixer.music.play()

	
		
	
			import smtplib
			
		
			if URLcounter > 0:		
				try:
					import smtplib
					from email.mime.multipart import MIMEMultipart
					from email.mime.text import MIMEText
					from email.mime.base import MIMEBase
					from email import encoders
					
					fromaddr = "cyberdefense1a2b3c@gmail.com"
					toaddr = EMAIL
					 
					msg = MIMEMultipart()
					 
					msg['From'] = fromaddr
					msg['To'] = toaddr
					msg['Subject'] = "Packet Information: %s "%time.asctime( time.localtime(time.time()))
					 
					body = "\nThe website(%s) has been entered %d times out of %s other packets.\nThe capture was done from %s to %s"%(URL,URLcounter,int(lines[-10]),currenttime,datetime.datetime.now().time())
					 
					msg.attach(MIMEText(body, 'plain'))
					 
					filename = "TestURL.txt"
					attachment = open("/root/Desktop/TestURL.txt", "rb")
					 
					part = MIMEBase('application', 'octet-stream')
					part.set_payload((attachment).read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
					 
					msg.attach(part)
					 
					server = smtplib.SMTP('smtp.gmail.com', 587)
					server.starttls()
					server.login(fromaddr, "cyberdefense")
					text = msg.as_string()
					server.sendmail(fromaddr, toaddr, text)
					server.quit()
					pass
				except:
					pass
			print("If you wish to stop, press Ctrl+C.")
			time.sleep(10)
	except KeyboardInterrupt:
		pass


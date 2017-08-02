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

print("If you would like to monitor people who enter certain websites, please do so by inputting URLs.")
print("If you are finished with inputting URLs or wish to not monitor any websites, press 1 to do so")


array_URL = list()
URLs = list()
URLinput = "0"
while URLinput != "1":
	
	URLinputCounter = 1
	URLinput = input("::")	
	try: 
		Inverse = socket.gethostbyname(URLinput)
		Reverse = socket.gethostbyname(Inverse)
		array_URL.append(Reverse)
		URLs.append(URLinput)
		URLinputCounter += 1
	except:
		print("Incorrect URL")


array_URL.remove('0.0.0.1')
URLs.remove('1')
print(array_URL)

if len(array_URL) is not 0:

	EMAIL = input("Please insert an email to sent notifications by email: ")

	if EMAIL:
		try:
			msg = "\nThank you, please wait as we prepare for packet scanning..."
			server.sendmail("cyberdefense1a2b3c@gmail.com",EMAIL,msg)
		except:
			msg = "\nEmail does not exist, please try again"
			os.system('python3 test3.py')

if not array_URL:
	array_URL = 'nothing'

if array_URL:
	currenttime = datetime.datetime.now().time()
	try: #this try statement will make the program run forever until you press Ctrl-C at the end
		URLcounter = 0
		datacount = open("URL.txt", "w")
		while True:
			from pygame import *	
			import time	
			import os
			import sys

	
	
	
			os.system('tshark -a duration:120 -T psml > TEST123.txt')#this will start tshark with a terminal command
	
			from collections import Counter #will count the highest used packet

			datain = open("TEST123.txt") 
			dataout = open("Main.txt", "w+")#these 2 lines will import and export packet data into a more readable format

			delete_list = ['<packet>','<section>','</section>','<structure>','</packet>','</structure>']
			for line in datain:
				for word in delete_list:
					line = line.replace(word,"")
				dataout.write(line)
			datain.close()
			dataout.close()

			f = open("Main.txt","r")

			

			lines = f.readlines() #Variable set to read a certain line. ex: lines[1] will read the first line of the text file

			data = []
			destIp = []
			sourceIp = []
			
			URLindividual = []
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
				
				
				"""print("No.",data[i][0],
				"\nTime:\t\t",data[i][1],
				"\nSource:\t\t",data[i][2],
				"\nDestination:\t",data[i][3],
				"\nProtocal:\t",data[i][4],
				"\nLength:\t\t",data[i][5],
				"\nInfo:\t\t",data[i][6],
				"\n")"""
			
			
			    	
				try:
		
					
					"""print("----------------------------------------------------")"""
					
					for f in range(len(array_URL)):
						if array_URL[f] in data[i][3]:	
			
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
							sourceIp.append(data[i][2])
							
							URLindividual.append(URLs[f])
						
						

											
				except:
					"""print("----------------------------------------------------")"""				
					pass
			

				if Destination[0].isalpha():
					destIp.append("Broadcast")
				else:
					destIp.append(Destination)

				
				# creating a counter
		
		
		
		
			counterList = Counter(destIp).most_common(1)
			
			
			mostOccuring = Counter(destIp).most_common(1)[0][1]
			
			sourceList = Counter(sourceIp).most_common(1)
			sourceList = dict(sourceList)
			
			URLaccessed = Counter(URLindividual)
			URLaccessed = dict(URLaccessed)
			
			print("The most common IPs",counterList)
			print("How many packets:",mostOccuring)
			print("The URL counter is: ", URLcounter)
			
			print(URLaccessed)
			
				
			
			

			if mostOccuring > 750:
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
					 
					body = "Dear piOT user,\n\t\t A user/Users has accessed the URLs specidifed.\nThe following websites you have specified have been accessed %d time(s):\n%s\n\nThe following Source IP addresses have accessed these URLs: \n%s\n\nIf you wish to know more about the IP addresses, have a look at the URL.txt attachemnt.\nIf you wish to know about everything that happened in the server, look at the Main.txt file instead.\n----------------------------------------------------\n Scan has been done from %s to %s"%(URLcounter,URLaccessed,sourceList,currenttime,datetime.datetime.now().time())		 
					msg.attach(MIMEText(body, 'plain'))
					 
					filename = "URL.txt"
					attachment = open("/root/Desktop/URL.txt", "rb")#please change this if on raspberry pi
					filename = "Main.txt"					
					attachment2 = open("/root/Desktop/Main.txt", "rb")
					 
					part = MIMEBase('application', 'octet-stream')
					part.set_payload((attachment).read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', "attachment; filename= URL.txt")
					

					part2 = MIMEBase('application', 'octet-stream')
					part2.set_payload((attachment2).read())
					encoders.encode_base64(part2)
					part2.add_header('Content-Disposition', "attachment; filename= Main.txt")
					

					msg.attach(part)
					msg.attach(part2)
					 
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
			os.remove("URL.txt")
			datacount = open("URL.txt", "w+")
			URLcounter = 0
	except KeyboardInterrupt:
		pass


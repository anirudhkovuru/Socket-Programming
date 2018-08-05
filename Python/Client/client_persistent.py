import socket                   

s = socket.socket()             
host = ""
port = 60001                

s.connect((host, port))
s.send("Hello server!")

#number of files to be received is sent to server
filenum = raw_input("Enter number of files to share: ")
s.send(filenum)
filenum = int(filenum)

for x in range(1, filenum+1):
	#sending file name
	fname = raw_input("Enter file name: ")
	s.send(fname)

	conf = s.recv(1024)
	print conf

	if conf == "file exists":
		length = 1024

		#sending confirmation for file exists
		s.send("Good")

		with open(fname, 'wb') as f:
			print 'file opened'
			while length >= 1024:
				#receiving the file size
				length = s.recv(8)
				print('length=%s', str(length))
				length = int(length)

				#sending confirmation
				s.send("Received length")

				print('receiving data...')

				#client receives file packet
				data = s.recv(length)
				print('data=%s', (data))

				f.write(data)

		f.close()
		print('Successfully got the file')

	else:
		continue


s.close()
print('connection closed')

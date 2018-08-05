import socket                   

s = socket.socket()             
host = ""
port = 60001                

#open new socket
s.connect((host, port))
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#sending the number of files
filenum = raw_input("Number of files: ")
s.send(str(filenum))
filenum = int(filenum)

#receive confirmation
conf = s.recv(1024)
print conf

#close socket
s.close()
print('connection closed\n')

for x in range(0, filenum):

	#opening a new socket
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.connect((host, port))

	#get file name from user and send to server
	fname = raw_input("Enter file name: ")
	s.send(fname)

	conf = s.recv(1024)
	print conf

	if conf == "file exists":
		s.send("Good")
		#opening file
		with open(fname, 'wb') as f:
			print 'file opened'
			while True:
				print('receiving data...')
				data = s.recv(1024)
				print('data=%s', (data))
				if not data:
					break
				# write data to a file
				f.write(data)

		f.close()
		print('Successfully got the file')

	#close the socket
	s.close()
	print('connection closed\n')

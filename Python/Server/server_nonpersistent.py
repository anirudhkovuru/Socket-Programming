import socket

port = 60001
host = ""

print 'Server listening....'

#open a new socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print 'Got connection from', addr

#receive the number of files
filenum = conn.recv(4)
print filenum
conn.send("Server received number of files")
filenum = int(filenum)

#close the connection
print('Done sending')
conn.close()
s.close()

for i in range(0, filenum):
	#open a new socket
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind((host, port))
	s.listen(5)
	conn, addr = s.accept()
	print 'Got connection from', addr

	#receive the name of file
	fname = conn.recv(1024)
	print fname
	fname = "./Data/" + fname

	#open file if exists
	try:
		f = open(fname,'rb')
		conn.send("file exists")

		conf = conn.recv(1024)

		l = f.read(1024)
		while (l):
			conn.send(l)
			print('Sent ',repr(l))
			l = f.read(1024)
		f.close()

	except:
		conn.send("file does not exist")
		print "file does not exist"

	#close the connection
	print('Done sending')
	conn.close()
	s.close()
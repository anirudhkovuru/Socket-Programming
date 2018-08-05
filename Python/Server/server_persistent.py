import socket

port = 60001
s = socket.socket()
host = ""

s.bind((host, port))
s.listen(5)

#server has started
print 'Server listening....'

#server has accepted a connection
conn, addr = s.accept()

#printing first message received from client
print 'Got connection from', addr
data = conn.recv(1024)
print data
print('Server received', repr(data))

#number of files received
i = conn.recv(1024)
i = int(i)
print i
print('Number of files to be sent received', repr(i))

for x in range(1, i+1):
    #conn, addr = s.accept()
    #print 'Got connection from', addr
    #data = conn.recv(1024)
    #print data
    #print('Server received', repr(data))

    #received file name
    fname = conn.recv(1024)
    print fname
    print('File name received', repr(fname))
    fname = "./Data/" + fname

    #fname exists
    try:
    	f = open(fname,'rb')

    	#sending file status
    	conn.send("file exists")

    	#receive confirmation
    	confn = conn.recv(1024)
    	print confn

    	l = f.read(1024)
    	length = 1024

    	while (l):
        	#get length of file and send to client
        	length = len(l)
        	conn.send(str(length))

        	#receive confirmation
        	conf = conn.recv(1024)
        	print conf

        	#sending the file packet to client
        	conn.send(l)
        	print('Sent ',repr(l))

        	l = f.read(1024)

    	f.close()

    #fname does not exist
    except:
    	conn.send("file does not exist")
    	print "file does not exist\n"

print('Done sending')
conn.send('Thank you for connecting')
conn.close()

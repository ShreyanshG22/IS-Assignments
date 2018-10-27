import socket
import json
from owncrypt import decryption

def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 2221
		s = socket.socket()
	except socket.error as err:
		print("Creation Error" + str(err))

#Bind
def socket_bind():
        try:
                global host
                global port
                global s
		print("Bind to " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as err:
		print("Bind error",str(err),"\n")
		#socket_bind()

#Accept Connection
def socket_accept():
	conn, add = s.accept()
	print("Connected to",add[0],":",str(add[1]))
	server_program(conn)
	conn.close()

def server_program(conn):
	username = "shreyansh"
	password = "ISAssign4"
	while True:
		data = conn.recv(1024)
		if not data:
			break
		data = decryption(data).split()
		print(" Received Data : ")
		print(" Username = " + str(data[0]))
		print(" Password = " + str(data[1]))
		if data[0] == username and data[1] == password:
			data = "Validation Successful!"
		else:
			data = "Invalid Username/Password"
		conn.send(data.encode())
	conn.close()
	
def main():
	socket_create()
	socket_bind()
	socket_accept()

main()

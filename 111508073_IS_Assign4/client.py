import socket
from owncrypt import encryption

def client_program(soc):
	username = raw_input(" Username -> ")
	password = raw_input(" Password -> ")
	data = username + " " + password
	data = encryption(data)
	soc.sendall(data)
	data = soc.recv(1024).decode()
	print(' Response from server: ' + data)
	soc.close()
	
def main():
	host = socket.gethostname()
	port = 2221
	soc = socket.socket()
	soc.connect((host, port))
	client_program(soc)
main()

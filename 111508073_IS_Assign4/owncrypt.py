def decryption(line):
	r = line.split(" ")
	h = ""
	for i in r:
		l = len(i)
		for k in range(l):
			h += chr((ord(i[k]) - l + k)%255)
		h += " "
	return h
	
def encryption(line):
	r = line.split(" ")
	h = ""
	for i in r:
		l = len(i)
		for k in range(l):
			h += chr((ord(i[k]) + l - k)%255)
		h += " "
	return h


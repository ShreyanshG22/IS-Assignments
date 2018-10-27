def decryption(line):
	r = line.split(" ")
	h = ""
	for i in r:
		l = len(i)
		for k in range(l):
			h += chr((ord(i[k]) - l + k)%255)
		h += " "
	return h

def main():
	f = open("encryption.txt", 'r')
	fw = open("decryption.txt", 'w')
	lines = f.readlines()
	lines = [l.strip() for l in lines]
	for l in lines:
		fw.write(decryption(l))
		fw.write("\n")
	f.close()
	fw.close()
main()

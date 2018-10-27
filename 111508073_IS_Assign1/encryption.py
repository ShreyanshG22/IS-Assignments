import sys

def encryption(line):
	r = line.split(" ")
	h = ""
	for i in r:
		l = len(i)
		for k in range(l):
			h += chr((ord(i[k]) + l - k)%255)
		h += " "
	return h

def main():
	f = open(sys.argv[1], 'r')
	fw = open("encryption.txt", 'w')
	lines = f.readlines()
	lines = [l.strip() for l in lines]
	for l in lines:
		fw.write(encryption(l))
		fw.write("\n")
	f.close()
	fw.close()
main()

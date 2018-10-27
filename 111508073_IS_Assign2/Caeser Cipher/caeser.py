def encryption(plaintext,key):
	h = ""
	for i in plaintext:
		for j in range(len(i)):
			if (i[j].isupper()):
				h += chr((ord(i[j]) + key - 65)%26 + 65)
			else:
				h += chr((ord(i[j]) + key - 97)%26 + 97)
		h += " "
	return h
	
def decryption(plaintext,key):
	h = ""
	for i in plaintext:
		for j in range(len(i)):
			if (i[j].isupper()):
				h += chr((ord(i[j]) - key - 65)%26 + 65)
			else:
				h += chr((ord(i[j]) - key - 97)%26 + 97)
		h += " "
	return h

def main():
	i = int(raw_input("Integer key: "))
	l = raw_input("Plaintext: ")
	encrypt = encryption(l.strip().split(" "),i)
	print "Caeser Cipher:\t",encrypt,"\nDecryption:\t",decryption(encrypt.strip().split(" "), i)
main()

def encryption(plaintext, key):
	h = ""
	l = len(plaintext)
	p = key + plaintext
	for i in range(l):
		h += chr((ord(plaintext[i]) - 97 + ord(p[i]) - 97)%26 + 97)
	return h
	
def main():
	j = raw_input("Key Word: ")
	k = raw_input("Plaintext without spaces: ").split(" ")
	k = "".join(k)
	print "Autokey Cipher:\t",encryption(k.lower(),j.lower())
main()

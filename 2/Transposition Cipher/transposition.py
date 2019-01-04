def encryption(text, key):
	k = len(key)
	t = len(text)
	if t%k > 0:
		text += 'z'*(k - t%k)
	t = len(text)
	temp = list(key)
	index = sorted(temp)
	ind = [index.index(i) for i in key]
	pak = list(set(ind))
	if len(pak) != len(ind):
		afg = [i for i in range(k)]
		aus = [i for i in afg if i not in pak]
		inp = []
		g = 0
		for i in ind:
			if i not in inp:
				inp.append(i)
			else:
				inp.append(aus[g])
				g += 1
		ind = inp
	cipher_text = ['a']*t
	counter = 0
	row_no = 0
	rows = t/k
	for i in range(t):
		cipher_text[rows*ind[i%k]+row_no] = text[i]
		if (i+1) % k == 0 :
			row_no += 1 
	return "".join(cipher_text), ind

def decryption(text, ind):
	lst = list(text)
	rows = len(lst)/len(ind)
	k = len(ind)
	ind = [str(i) for i in ind]
	o = sorted(ind)
	op = "".join(o)
	j = 0
	p = 0
	inj = [ind.index(i) for i in op]
	for i in range(len(text)):
		lst[p*k + inj[j]] = text[i]
		p += 1
		if (i + 1)%rows == 0:
			p = 0
			j += 1
	return "".join(lst)

def main():
	key = raw_input("Enter Key: ")
	text = raw_input("Enter Plaintext: ")
	encrypt, ing = encryption(text, key)
	print "Ciphertext:",encrypt,"\nDecrypted Text:",decryption(encrypt, ing)
main()

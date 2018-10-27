from math import sqrt
import numpy
import gmpy2
import sys

character = "abcdefghijklmnopqrstuvwxyz"
letter = dict([(character[i], i) for i in range(len(character))])

def modinv(a_f, m = 26):
    f = numpy.copy(a_f)
    assert isinstance(f, numpy.ndarray)
    assert isinstance(m, int)
    n = a_f.shape[0]
    g = numpy.identity(n, dtype=int)
    for i in range(n):
        for j in range(i+1,n):
            try:
                gmpy2.invert(int(f[j,i]), m)
                f[i], f[j] = numpy.copy(f[j]), numpy.copy(f[i])
                g[i], g[j] = numpy.copy(g[j]), numpy.copy(g[i])
                break
            except:
		pass
        try:
        	inv = int(gmpy2.invert(int(f[i,i]), m))
        except ZeroDivisionError:
                print("Inverse is not possible for the key")
                return []

        f[i] = f[i] * inv % m
        g[i] = g[i] * inv % m
        for j in range(n):
            if j != i:
                p = f[j,i]
                f[j] = (f[j] - f[i] * p) % m
                g[j] = (g[j] - g[i] * p) % m
    assert numpy.array_equal(f, numpy.identity(n, dtype=int))
    assert numpy.array_equal(a_f.dot(g) % m, numpy.identity(n, dtype=int))
    assert isinstance(g, numpy.ndarray)
    return g

def hill(text, key, decrypt = False):
	n = int(sqrt(len(key)))
	if n*n!=len(key):
		print("Key length should have a square root")
		return
	if len(text)%n > 0:
		text += 'x'*(n - (len(text)%n))

	klist = []
	for char in key:
		klist.append(letter[char])
	keymatrix = [] 
	for i in range(n):
		keymatrix.append(klist[i * n : i * n + n])
		
	lst = []
	for i in range(n):
		k = []
		for a in text[i*(len(text)/n):i*(len(text)/n)+(len(text)/n)]:
			k.append(letter[a])
		lst.append(k)
	lst = numpy.array(lst)
	keymatrix = numpy.array(keymatrix)
	if decrypt == True:
		keymatrix = modinv(keymatrix)
		if keymatrix == []:
			return
	res = numpy.dot(keymatrix,lst).round()
	result = ""
	result += ''.join([character[int(item)%26] for j in res for item in j])
	return result

def main():
	key = raw_input("Enter Key:")
	if sys.argv[1] == "-e":
		f = open(sys.argv[2], 'r')
		fw = open("encryption.txt", 'w')
		lines = f.readlines()
		lines = [l.strip() for l in lines]
		for l in lines:
			fw.write(hill(l,key))
			fw.write("\n")
		f.close()
		fw.close()
	elif sys.argv[1] == "-d":
		f = open(sys.argv[2], 'r')
		lines = f.readlines()
		lines = [l.strip() for l in lines]
		for l in lines:
			print(hill(l, key, True))
		f.close()
	else:
		print("Usage:\tpython hill.py -e/d <filename>")
main()

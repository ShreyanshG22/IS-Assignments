sbox  = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]
sboxInv = [0xa, 0x5, 0x9, 0xb, 0x1, 0x7, 0x8, 0xf, 0x6, 0x0, 0x2, 0x3, 0xc, 0x4, 0xd, 0xe]

w = [None]*6
K = [None]*3

def subnibble(M, sBox):
	for i in range(len(M)):
			M[i] = sBox[M[i]]
	return M

def shiftRows(M):
	return [M[0],M[1],M[3],M[2]]

def mixColumn(M, Inv = False):
	def mult(a, b):
		k = 0
		while b:
			if b & 0b1:
				k ^= a
			a <<= 1
			if a & 0b10000:
				a ^= 0b11
			b >>= 1
		return k & 0b1111
	if Inv:
		M = [mult(9,M[0])^mult(2,M[2]), mult(9,M[1])^mult(2,M[3]), mult(9,M[2])^mult(2,M[0]), mult(9,M[3])^mult(2,M[1])]
	else:
		M = [M[0]^mult(4,M[2]), M[1]^mult(4,M[3]), M[2]^mult(4,M[0]), M[3]^mult(4,M[1])]
	return M

def addRoundKey(M, Key):
	return (M^Key)

def keyExpansion(Key):
	def sub2Nib(byte):
		return sbox[byte >> 4] + (sbox[byte & 0x0f] << 4)
	Rcon1, Rcon2 = 0b10000000, 0b00110000
	w[0] = (Key&0xff00) >> 8
	w[1] = Key&0x00ff
	w[2] = w[0] ^ Rcon1 ^ sub2Nib(w[1])
	w[3] = w[2] ^ w[1]
	w[4] = w[2] ^ Rcon2 ^ sub2Nib(w[3])
	w[5] = w[4] ^ w[3]
	for i in range(3):
		K[i] = (w[i]<<8)+w[i + 1]
	return K

def encrypt(M, key):
	K = keyExpansion(key)
	text = ((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3])
	M = addRoundKey(text, K[0])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	M = mixColumn(shiftRows(subnibble(M, sbox)))
	M = addRoundKey(((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3]), K[1])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	M = shiftRows(subnibble(M, sbox))
	M = addRoundKey(((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3]), K[2])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	return chr((M[0]<<4)+M[1])+chr((M[2]<<4)+M[3])

def decrypt(M, key):
	text = ((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3])
	M = addRoundKey(text, K[2])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	M = subnibble(shiftRows(M), sboxInv)
	M = addRoundKey(((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3]), K[1])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	M = mixColumn(M, True)
	M = subnibble(shiftRows(M), sboxInv)
	M = addRoundKey(((M[0] << 12) + (M[2] << 8) + (M[1] << 4) + M[3]), K[0])
	M = [M >> 12, (M >> 4) & 0xf, (M >> 8) & 0xf,  M & 0xf]
	return chr((M[0]<<4)+M[1])+chr((M[2]<<4)+M[3])

def main():
	plaintext = raw_input("Enter plaintext: ")
	key = raw_input("Enter key: ")
	if len(key)!=2:
		print("Please enter 16bit key only")
	if len(plaintext)%2 > 0:
		plaintext += "z"
	key = (ord(key[0])<<8) + ord(key[1])
	#key = 0b1010011100111011
	string = ""
	for i in range(0,len(plaintext),2):
		string += encrypt([(ord(plaintext[i])>>4)&0xf, ord(plaintext[i])&0xf,(ord(plaintext[i + 1])>>4)&0xf, ord(plaintext[i + 1])&0xf], key)
	print("Encrypted Text: "+string)
	st = ""
	for i in range(0,len(plaintext),2):
		st += decrypt([(ord(string[i])>>4)&0xf, ord(string[i])&0xf,(ord(string[i + 1])>>4)&0xf, ord(string[i + 1])&0xf], key)
	print("Decrypted Text: "+ st)
main()

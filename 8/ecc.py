def modInverse(a, m) :
	a = a % m;
	for x in range(1, m) :
		if ((a * x) % m == 1) :
			return x
	return 1

def addition(x1, y1, x2, y2, field):
	xd = (x2 - x1)
	xf = modInverse(xd, field)
	slope = (y2 - y1) * xf
	slope = slope % field
	xnew = (slope * slope - x1 - x2) % field
	ynew = (-y1 + slope * (x1 - xnew)) % field
	temp = [xnew, ynew]
	return temp
	
def doubling(x, y, field):
	s_num = (3 * x * x + 1)
	s_deno = modInverse(2 * y, field)
	s = (s_num * s_deno) % field
	xnew = (s * s - 2 * x) % field
	ynew = (-y + s *(x - xnew)) % field
	temp = list()
	temp.append(xnew)
	temp.append(ynew)
	return temp

def main():
	a = int(raw_input("a = "))
	b = int(raw_input("b = "))
	if(4*a*a*a + 27*b*b == 0):
		print("Invalid parameters a & b")
		return
	field = int(raw_input("Enter the prime field : "))
	
	i = "y"
	while(i == "y"):
		print("Operations:\n0:Generate Keys For Diffie Hellman Key Exchange\n1:Point negation\n2:Point addition\n3:Point doubling\n4:Check whether point lies on curve\n")
		operation = int(raw_input("Enter the corresponding number: "))
		if operation == 0:
			a = int(raw_input("Enter Private Key for Alice:"))
			b = int(raw_input("Enter Private Key for Bob:"))
			print("Enter the generator point:")
			x = int(raw_input("x coordinate - "))
			y = int(raw_input("y coordinate - "))
			x1, y1 = doubling(x, y, field)
			for i in range(a-1):
				x1, y1 = addition(x1, y1, x, y, field)
			print("Public Key for Alice: (" + str(x1)+","+str(y1)+")")
			x2, y2 = doubling(x, y, field)
			x3, y3 = addition(x1, y1, x, y, field)
			for i in range(b-1):
				x2, y2 = addition(x2, y2, x, y, field)
				x3, y3 = addition(x3, y3, x, y, field)
			print("Public Key for Bob: (" + str(x2)+","+str(y2)+")")
			print("Session Key Shared: (" + str(x3)+","+str(y3)+")")
		elif operation == 1:
			print("Enter the point:")
			x = int(raw_input("x coordinate - "))
			y = int(raw_input("y coordinate - "))
			ynew = (-y) % field
			print("Negation of point : (" + str(x) + "," + str(ynew) + ")") 
		elif operation == 2:
			print("First point:")
			x1 = int(raw_input("x coordinate - "))
			y1 = int(raw_input("y coordinate - "))
			print("Second point:")
			x2 = int(raw_input("x coordinate - "))
			y2 = int(raw_input("y coordinate - "))
			if (x1 == -x2 and y1 == -y2):
				xnew, ynew = 0, 0
			elif (x1 == x2 and y1 == y2):
				xnew, ynew = doubling(x1, y1, field)
			else:
				xnew, ynew = addition(x1, y1, x2, y2, field)
			print("Addition of points : (" + str(xnew) + "," + str(ynew) + ")")
		elif operation == 3:
			print("Enter the point:")
			x = int(raw_input("x coordinate - "))
			y = int(raw_input("y coordinate - "))
			xnew, ynew = doubling(x, y, field)
			print("Doubled point : (" + str(xnew) + "," + str(ynew) + ")")
		elif operation == 4:
			print("Enter the point:")
			x = int(raw_input("x coordinate - "))
			y = int(raw_input("y coordinate - "))
			lhs = (y * y) % field
			rhs = (x*x*x + a*x + b) % field
			if lhs == rhs:
				print("Point lies on the curve")
			else:
				print("Point doesn't lie on the curve")
		else:
			print("Invalid Operation Selection!!")
			continue
		print("\nDo you want to continue : y/n")
		i = raw_input().lower()
	return
main()


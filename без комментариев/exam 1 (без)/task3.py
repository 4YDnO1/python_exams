a = float(input())
b = float(input())

c = input()

res = ''

if (c == "+"):
	res = a + b
elif (c == "-"):
	res = a - b
elif (c == "*"):
	res = a * b
elif (c != "pow" and b == 0 ) or (a == 0 and b < 0):
	res = "Zero Division Error!"
elif (c == "/"):
	res = a / b
elif (c == "mod"):
	res = a % b
elif (c == "pow"):
	res = a ** b 
elif (c == "div"):
	res = a // b
	
if (res != ''):
	print(res)
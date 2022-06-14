n = int(input())

res = ''

i = 0
j = 1

while i != n:
	k = 0
	while i != n and k != j:
		res += str(j) + ' '
		i += 1
		k += 1
	j += 1
	
print(res)

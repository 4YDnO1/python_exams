a = input().split(' ')
n = int(input())

res = []
index = 0

while index < len(a):
	if (int(a[index]) == n):
		res.append(str(index))
	index += 1

if (len(res)):
	print(" ".join(res))
else:
	print("Отсутствует")
a = int(input())
b = int(input())
c = int(input())

if (a >= b >= c):
	print("%s\n%s\n%s" % (a, c, b))
elif (a >= c >= b):
	print("%s\n%s\n%s" % (a, b, c))
elif (b >= a >= c):
	print("%s\n%s\n%s" % (b, c, a))
elif (b >= c >= a):
	print("%s\n%s\n%s" % (b, a, c))
elif (c >= a >= b):
	print("%s\n%s\n%s" % (c, a, b))
else:
	print("%s\n%s\n%s" % (c, b, a))



#--- Начало программы. Вариант "сложный"
'''
a = [int(input()) for i in range(3)]; a.sort()
print("%s\n%s\n%s" % (int(a[2]), int(a[0]), int(a[1])))
'''
#--- Конец программы. Вариант "сложный"
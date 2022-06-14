n = int(input())

if (n % 10 == 1) and (n % 100 != 11):
    print(n, 'программист')
elif (n % 10 >= 2) and (n % 10 <= 4) and (n % 100 < 10 or n % 100 > 20): 
    print(n, 'программиста')
else:
    print(n, 'программистов')
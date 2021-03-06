#---
#--- Задача 7. Экз №1
#--- Проверка 6-ти значного числа (номера) на "счастливость"
#--- т.е. сумма 1-ой половины равна 2-ой

#--- !! Присутствует 2 решения


#--- Начало программы. Простой вариант. Оптимизированный

n = input()

#--- Нет необходимости разделять по переменным значения
#--- Достаточно сложить цифры числа по индексу
#--- предварительно преобразовав в целочисленное значение int()

#--- Проверка и вывод в зависимости от результата соответсвенно
if (int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5])):
    print("Счастливый")
else:
	print("Обычный")

#--- Конец программы. Простой вариант. Оптимизированный




#--- Начало программы. Продвинутый вариант

#--- Запишем переменную как массив цифр,
#--- распилив число в виде строки с помощью .split()
n = input().split()

#--- Всё таже, проверка и вывод, но только
#--- теперь складывание производим при помощт функции sum()
#--- сделав выборку с помощтю вырезки из массива [:]
#--- [начало : 3 индекс], [3 индекс : конец]

if (sum(n[:3]) == sum(n[3:])):
    print("Счастливый")
else:
	print("Обычный")

#--- Конец программы. Продвинутый вариант
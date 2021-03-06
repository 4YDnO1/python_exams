#---
#--- Задача 2. Экз №1
#--- Определение, входит-ли число в указанный диапазон
#--- Диапазон: (-15, 12] U (14, 17) U [19, +беск)
#--- Где "(", ")" = это не включительные границы, т.е. "<" или ">",
#--- а "[", "]" = это включительные границы, т.е. "<=" или ">="
#--- "U" выступает в качестве оператора "OR"/"или", объединяя участки диапазона
#---

#--- Начало программы

#--- Чтение вводимого числа a (проверяемое число) при помощи input()
#--- int() - преобразование из вводмиого "текста" в целочисленное
a = int(input())

#--- Вывод на экран результат "выражения-проверки"
#--- Нет необходимости делать конструкцию ветвления ( if | else)
#--- т.к. результатом операций с логическими операндами...
#--- является "True" (истина) и "Flase" (ложь)
#--- Достаточно вывести этот результат при помощт print()
print( (-15 < a <= 12) or (14 < a < 17) or (a >= 19) )

#--- Конец программы
#---
#--- Задача 4. Экз №2.
#--- Вычисление матрицы
#--- исходя из входной матрицы путём сложения
#--- 4-рёх соседних цифр (если нет с какой-либо из сторон,
#--- то брать с другой стороны матрицы)
#---
#--- !! Достаточно интересное задание, по хорошему распилить на функции
#--- но не будем)))
#---
#--- !! Для записи|чтения матриц будем использовать
#--- двумерные массивы проходя по ним по координатам,
#--- столбцу (x) и строке (y)
#---

#--- Начало программы

#--- Иницилизируем массив для записи массивов (строк)
matrix = []

#--- бесконечный цикл для ввод сколько-угодной матрицы
while True:
	#--- считываем строку
	row = input()

	#--- усли это не конец, запишем строку в матрицу
	#--- разделив строчку текста на столбцы
	if (row == 'end'):
		break
	else:
		matrix.append(row.split(' '))

#--- Создадим дополнительные параметры для простоты понимания

#--- Конечный индекс эллемента в столбце
yend = len(matrix) - 1
#--- Конечный индекс эллемента в строке
xend = len(matrix[0]) - 1

#--- Для начальных нет необходимости их писать
#--- т.к. это всегда 0 лул :D

#--- !! Не будем создавать новый массив для записи результата
#--- т.к. это не указано в задаии, просто переберём введённый
#--- попутно расчитывая новые значения, записывая в мамссив
#--- строки и сразу выводя её, как только она готова

#--- перебирать будем с помощью двух цмклов (ещё бы,
#--- это ведь матрица (двумерный массив))

#--- Внешний цикл, отвечает за строки (y)
for y in range(0, len(matrix)):

	#--- Иницилизируем массив для записи новой строчки
	newRow = []

	#--- Внутрений цикл, отвечает за колонки (x)
	for x in range(0, len(matrix[y])):

		#--- найдём соседние для текущей ячейки матрицы
		#--- по часовой стрелке

		#--- Проверяем существует-ли ячейка выше, если нет,
		#--- берём с конца в этом столбце
		if ( y - 1 >= 0 ):
			up =  matrix[y - 1][x]
		else:
			up =  matrix[yend][x]

		#--- Проверяем существует-ли ячейка справа, если нет,
		#--- берём с начала в этой строке
		if (x + 1 <= xend):
			right =  matrix[y][x + 1]
		else:
			right =  matrix[y][0]

		#--- Проверяем существует-ли ячейка снизу, если нет,
		#--- берём с начала в этом столбце
		if (y + 1 <= yend):
			down =  matrix[y + 1][x]
		else:
			down =  matrix[0][x]

		#--- Проверяем существует-ли ячейка слева, если нет,
		#--- берём с конца в этой строке
		if (x - 1 >= 0):
			left =  matrix[y][x - 1]
		else:
			left =  matrix[y][xend]

		#--- Считаем значение "новой" ячейки
		cell = int(up) + int(right) + int(down) + int(left)

		#--- Добовляем значение в строчку, преобразовав строчку
		#--- опять же, что бы удобнее вывести потом join'ом
		newRow.append(str(cell))

	#--- После того как внеший цикл пройдёт по строчке матрицы
	#--- и заполнит новую строчку новыми значениями, (масло масленное)
	#--- выводим её, соединив join'ом
	#--- опять же, в цикле мы преобразововали в значения в строчные
	#--- чтобы мы смоги их соединить сейчас
	print(" ".join(newRow))

#--- Конец программы
matrix = []

while True:

	row = input()
	if (row == 'end'):
		break
	else:
		matrix.append(row.split(' '))

yend = len(matrix) - 1
xend = len(matrix[0]) - 1

for y in range(0, len(matrix)):
	newRow = []
	
	for x in range(0, len(matrix[y])):
		if ( y - 1 >= 0 ):
			up =  matrix[y - 1][x]
		else:
			up =  matrix[yend][x]

		if (x + 1 <= xend):
			right =  matrix[y][x + 1]
		else:
			right =  matrix[y][0]

		if (y + 1 <= yend):
			down =  matrix[y + 1][x]
		else:
			down =  matrix[0][x]

		if (x - 1 >= 0):
			left =  matrix[y][x - 1]
		else:
			left =  matrix[y][xend]

		cell = int(up) + int(right) + int(down) + int(left)
		newRow.append(str(cell))

	print(" ".join(newRow))
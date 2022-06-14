n = int(input())

matrix = []

for y in range(n):
	newRow = [] 
	for x in range(n): 
		newRow.append(0)
	matrix.append(newRow)


number = 1
corners = -1
cells = n - 1
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dirIndex = 1
dir = moves[dirIndex]
x, y = 0, 0
matrix[y][x] = str(number)

while cells != 0:

	for i in range(0, cells):
		number += 1
		y += dir[0]
		x += dir[1]

		matrix[y][x] = str(number)

	corners += 1

	if (dirIndex + 1 < 4):
		dirIndex += 1
		dir = moves[dirIndex]
	else:
		dirIndex = 0
		dir = moves[dirIndex]
	
	if corners == 2:
		corners = 0
		cells -= 1

for row in matrix: 
   print(" ".join(row))
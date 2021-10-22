# 1. Найти максимальный среди всех элементов тех строк заданной матрицы,
# которые упорядочены (либо по возрастанию, либо по убыванию).

matrix = []
need_stop = False

while not need_stop:
    s = input()
    if s != '':
        split = s.split(' ')
        tmp = []
        for j in split:
            tmp.append(int(j))
        matrix.append(tmp)
    else:
        need_stop = True

sortedIndex = []
for i in range(len(matrix)):
    for j in range(len(matrix[0]) - 1):
        if matrix[i][j] < matrix[i][j + 1]:
            if j == (len(matrix[0]) - 2):
                sortedIndex.append(i)
        else:
            break

for i in range(len(matrix)):
    for j in range(len(matrix[0]) - 1):

        if matrix[i][j] > matrix[i][j + 1]:
            if j == (len(matrix[0]) - 2):
                sortedIndex.append(i)
        else:
            break

maximum = -99999
for i in sortedIndex:
    for j in range(len(matrix[0])):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print("Maximum = ", maximum)

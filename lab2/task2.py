# 2. Дана прямоугольная матрица A[N, N].
# Переставить первый и последний столбцы местами и вывести на экран.

n = int(input())
matrixA = []

for i in range(0, n):
    subarray = []
    for j in range(0, n):
        subarray.append(int(input()))
    matrixA.append(subarray)

for i in range(0, n):
    tmp = matrixA[i][0]
    tmp2 = matrixA[i][n-1]
    matrixA[i][0] = tmp2
    matrixA[i][n-1] = tmp

for i in range(0, n):
    print("", end='\n')
    for j in range(0, n):
        print(matrixA[i][j], end=' ')

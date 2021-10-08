# 1. Дана целая квадратная матрица n-го порядка.
# Определить, является ли она магическим квадратом,
# т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.

n = int(input())
matrix = []

i = 0
j = 0
for i in range(0, n):
    subarray = []
    for j in range(0, n):
        subarray.append(int(input()))
    matrix.append(subarray)

i = 0
j = 0
sumStr = []
for i in range(0, n):
    summ = 0
    for j in range(0, n):
        summ += matrix[i][j]
    sumStr.append(summ)

i = 0
j = 0

sumStolb = []
for i in range(0, n):
    summ = 0
    for j in range(0, n):
        summ += matrix[j][i]
    sumStolb.append(summ)

i = 0
for i in range(0, len(sumStr)):
    if sumStr[i] != sumStolb[i]:
        print("Это не магический квадрат!")
        exit(0)
print("Это магический квадрат!")

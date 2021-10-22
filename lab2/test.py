# 1. Задана квадратная матрица. Переставить строку с максимальным
# элементом на главной диагонали со строкой с заданным номером m.
n = int(input())
m = int(input())
matrix = []

for i in range(0, n):
    subarray = []
    for j in range(0, n):
        subarray.append(int(input()))
    matrix.append(subarray)

n = 0
b = 0

for i in range(len(matrix)):
    if matrix[i][i] > b:
        b = matrix[i][i]
        n = i

massiv_a = matrix[n]
massiv_b = matrix[m-1]

matrix[n] = massiv_b
matrix[m-1] = massiv_a

print(massiv_a)
print(massiv_b)

# for i in range(0, n):
#     print("", end='\n')
#     for j in range(0, n):
#         print(matrix[i][j], end=' ')
for i in matrix:
    print(*i)
# 2. Составить программу, которая заполняет квадратную матрицу порядка
# с натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по спирали».
# Например, для п = 5 получаем следующую матрицу:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 14 12 11 10 9

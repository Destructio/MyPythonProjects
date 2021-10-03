# 2. Дан массив целых чисел.
# Переписать все положительные элементы во второй массив, а остальные - в третий.

n = int(input())

array = []
array2 = []
array3 = []

i = 0
for i in range(0, n):
    array.append(int(input()))

i = 0
for i in range(0, n):
    if array[i] >= 0:
        array2.append(array[i])
    else:
        array3.append(array[i])

print(array)
print(array2)
print(array3)

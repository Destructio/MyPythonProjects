# 1. Дан одномерный массив, состоящий из N целочисленных элементов.
# Ввести массив с клавиатуры.
# Найти минимальный элемент.
# Вывести индекс минимального элемента на экран.


n = int(input())
array = []

i = 0
for i in range(0, n):
    array.append(int(input()))

i = 0
minValue = 9999
index = 0
for i in range(0, n):
    if array[i] < minValue:
        minValue = array[i]
        index = i
print(index)

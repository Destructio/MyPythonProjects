# 7 (17) Вар
# Вводятся оценки студента в одну строчку через пробел.
# Необходимо сформировать словарь, в котором ключами являются оценки (числа), а значениями – количество этих оценок во введенном списке.
# Результат вывести на экран.

dictionary = {}
grades = []

need_stop = False

while not need_stop:
    s = input()
    if s != '':
        split = s.split(' ')
        for j in split:
            grades.append(int(j))
    else:
        need_stop = True

for i in range(len(grades)):
    grade = grades[i]
    count = 1
    for j in range(len(grades)):
        if grade == grades[j] and j != i:
            count = count + 1
    dictionary[grade] = count

print(dictionary)

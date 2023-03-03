# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

N = int(input("Введите количество элементов в массиве: "))

A = [random.randrange(10) for _ in range(N)]
print(f'{A = }')
x = int(input("введите число, количество повторений которого нужно найти: "))

count = 0
for i in A:
    if i == x:
        count += 1
print(f'Число {x} встречается в массиве {count} раз')

# вариант 2

print(*A)                # вывод списка без скобок через пробел (распаковка итерируемого объекта)
print(A.count(int(x)))   # метод count
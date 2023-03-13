# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random

list_a = [random.randint(0, 10) for i in range(10)]
print(*list_a)
double = []
list_a = sorted(list_a)
print(*list_a)
for i in range(len(list_a[1:])):
    if list_a[i - 1] == list_a[i] != list_a[i + 1]:
        double.append(list_a[i])
    if list_a[i - 2] == list_a[i - 1] == list_a[i] == list_a[i + 1]:
        double.append(list_a[i])
if list_a[len(list_a) - 2] == list_a[len(list_a) - 1]:
    double.append(list_a[i])
print(*double)
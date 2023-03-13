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
for i in range(len(list_a[: -1])):
    if list_a[i] == list_a[i + 1]:
        double.append(list_a[i])
    if list_a[i - 1] == list_a[i] == list_a[i + 1]:
        double.append(list_a[i - 1])
    if list_a[i - 2] == list_a[i] == list_a[i + 1]:
        double.append(list_a[i - 2])
print(len(double))

# вариант 2
count = 0
n = len(list_a)
for i in range(len(list_a[: n - 1])): # идем по значениям с первого элемента до предпоследнего
    for j in range(i + 1, n): # идем по значениям со следующего после i элемента до последнего
        if list_a[i] == list_a[j]:
            count += 1
print(count)

#вариант 3
cnt = 0
for j in range(len(list_a)):
    cnt += list_a[j + 1:].count(list_a[j])
print(list_a, cnt)

# вариант 4
def func(lst: list) -> int:
    el, *lst = lst # el = lst[0], lst = [1:]
    if lst: # пока список не пустой
        return func(lst) + lst.count(el)
    return 0

if __name__ ** '__main__':
    print(func([1, 2, 3, 2, 3]))
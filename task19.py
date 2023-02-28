# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения списка или 
# список задан изначально.

# вариант 1 (работатет только для статического списка, который уже задан)
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input("введите на какое количество элементов необходимо сдвинуть последовательность: "))
n = len(list_1)
new_list = list_1[-k:n] + list_1[:-k]
print(list_1)
print(new_list)

# вариант решения 2

a = [1, 2, 3, 4, 5, 6]
b = [0] * len(a)
k = 3
n = k % len(a)
for i in range(len(a)):
    b[i] = a[i - n]
print(a)
print(b)

# вариант 3
import random

N = 10

lst = [random.randrange(10) for _ in range(N)]
print(f'{lst = }')

k = int(input('k = '))
for _ in range(k):
    lst.insert(0, lst.pop())

print(f'{lst = }') #когда нужно вывести значение переменной с ее именем (функционал самодокументации)
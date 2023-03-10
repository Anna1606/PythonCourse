# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# вариант один (использование рекурсии как инструмент, для записи чисел в обратном порядке, а не по прямому назначению)
N = int(input('Введите число: '))
def rec_bac(n):
    if n == 0:
        return
    else:
        i = int(input('число: '))
        rec_bac(n - 1)
        print(i, end = ' ') # введение переменной строки после запятой позволяет записывать полученные числа в строку
    
rec_bac(N)

# вариант два (использование рекурсии как рекурсия)
def foo(n):
    if n == 1:
        return input()
    n -= 1
    temp = foo(n)
    return input() + ' ' + temp

print(foo(int(input())))

# вариант три
from random import randrange
def func(n):
    if n == 0:
        return '-> '
    var = randrange(n)
    print(var, end=' ')
    return f'{func(n - 1)} {var}'

print(func(5))
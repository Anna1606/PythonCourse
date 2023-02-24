# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input('введите натуральное число больше 1: '))
fib1 = 1
fib2 = 1
count = 3
i = 0

while i < count - 2:
    fibonachi = fib1 + fib2
    fib1 = fib2
    fib2 = fibonachi
    if fibonachi == a:
        print(count)
        break
    elif fibonachi > a:
        print(-1)
        break
    i += 1
    count += 1  

# вариант 2 (стандартное решение)
c, d = 0, 1 
# двойное присваиваение - кортеж, достаточно поставить запятую
n = 2

while d < a:
    c, d = d, c + d
    n += 1

if d == a:
    print(n)
else:
    print(-1)
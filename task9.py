# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120

# вариант 1
n = int(input('Введите целое неотрицательное число: '))
factorial = 1
count = 1
while count <= n:
    factorial *= count
    count += 1
print(factorial)

# вариант 2 (шагаем в обратную сторону)
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
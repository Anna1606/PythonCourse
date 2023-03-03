# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

import random

max_number = 0
n = int(random.randint(0, 10))
lst = []
while n > 0:
    lst.append(n)
    n = int(random.randint(0, 10))
    if max_number < n:
        max_number = n
else:
    lst.append(n)
print(lst)
print(max_number)

# вариант 2
while (i := random.randrange(11)) != 0:
    lst.append(i)
lst.append(i)

print(lst)
print(max(lst))
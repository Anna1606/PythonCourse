# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

n = int(input('введите количество монет на столе: '))

a = [random.randint(0, 1) for i in range(n)]
print(a)
sum_1 = 0
sum_0 = 0
for i in range(n):
    if a[i] == 0: 
        sum_0 += 1
    else: 
        sum_1 += 1
if sum_0 < sum_1: 
    print(sum_0)
else: 
    print(sum_1)
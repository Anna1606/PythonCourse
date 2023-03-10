# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

journal = [1, 3, 3, 4, 4]
print(*journal)
n = len(journal)
# срезы работают быстрее, чем нахождение максимума и минимума функцией
min_, max_ = sorted(journal)[::n - 1]
# функция возвращает массив кортежей (индекс и значение)
for i, val in enumerate(journal):
    if val == max_:
        journal[i] = min_
print(max_, min_)
print(*journal)

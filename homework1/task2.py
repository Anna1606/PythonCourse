# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

summ = int(number / 100) + number % 10 + number % 100 / 10
print(int(summ))
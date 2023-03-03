# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

s = 'a a a b c a a d c d d'
s = s.split()
print(s)
new_s = []
for i in range(len(s)):
    new_s.append(s[i])
    count_i = new_s.count(new_s[i])
    if count_i > 1:
        s[i] += '_' + str(count_i - 1)
print(*s)
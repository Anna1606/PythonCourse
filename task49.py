# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    
def find_farthest_orbit(list_of_orbits):
    return max(list_of_orbits, key = lambda i: i[0] != i[1] and i[0] * i[1])
    # вариант 2
    #return max(list_of_orbits, key = lambda i: (i[0] != i[1]) * i[0] * i[1])
    # логическое выражение возвращает 0 если ложь, и 1 если тру, альтернатива использования оператора and

    # вариант 3
    # s = {}
    # for i in list_of_orbits:
    #     a, b = i
    #     if a != b:
    #         k = a * b
    #         s[k] = i
    # max_ = max(s, key= lambda x: x)
    # for q in s:
    #     if q == max_:
    #         return s[q]

    # вариант 4
    # def find_farthest_orbit(lst):
        # max = 0
        # max_i = 0
        # new_lst = enumerate(lst)
        # for i, (k, v) in new_lst: распакуем нумерованный список кортежей, где i это номер кортежа, k и v первая и вторая цифры кортежа
            # if k != v:
                # if k * v > max:
                    # max = k * v
                    # max_i = i
        # return lst[max_i]

print(*find_farthest_orbit(orbits))

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар 
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

lst = [1, 2, 3, 5, 8, 15, 23, 38]

# def even (lst):
#     new_lst = []
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append((i, i ** 2))
#     return new_lst
# print(even(lst))

# def select(f, col):
#     """возвращает список, в котором мы к каждому элементу применили функцию f"""
#     return [f(x) for x in col] 

# def where(f, col):
#     """возвращает только те значения, которые прошли проверку условия f(x)"""
#     return [x for x in col if f(x)]

res = map(int, lst) 
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.

# вариант 1 (алгоритмический)
# def same_by(characteristic, objects):
#     for i in range(len(objects)):
#         if characteristic(objects[i]) != characteristic(objects[i - 1]):
#             return False
#     return True

# вариант 2
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1

values = [0, 4, 6, 10]
if same_by (lambda x: x % 2, values):
    print('same')
else:
    print('different')

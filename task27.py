# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# text = input('Введите текст, в котором слова идут через пробел: ')

text = '''She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''
text = set(text.upper().split())

print(len(text))

# вариант 2
text2 = ''

for char in text:
    if char == " " or char.isalpha(): # метод, который находит буквенные символы
        text2 += char # добавляем в новую строку только пробелы и буквы, опуская другие символы

dct = {}

for word in text2.lower().split():
    dct[word] = ''

print(len(dct))
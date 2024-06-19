# f = open('file.txt', 'r', encoding='utf-8')
# for line in f:
#   print(line)

# f.close()

# f = open('file.txt', 'w', encoding='utf-8')
# f.write('Hello, world!')
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)

#--------------------------------------------------

# f1 = open('data.txt')
# print(f1.read(11))
# print(f1.read())
# print(type(f1.read()))
# f1.close()

# f1 = open('data.txt')
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1.close()

# f1 = open('data.txt')
# print(f1.readlines())

# nums = []
# for i in open('data.txt'):
#   nums.append (i[:- 1])
# print(nums) 

#----------------------------------------------------

# try:
#   f = open('new_txt')
#   print(f.read())

# except FileNotFoundError:
#   print('Файл не найден')

# except PermissionError:
#   print('Нет доступа к файлу')

# except Exception as e:
#   print(f'Произошла ошибка: {e}')

#------------------------------------------------------

# with open('file.txt', 'r', encoding='utf-8') as f:
#   content = f.read()

# with open('file (2).txt', 'w', encoding='utf-8') as f:
#   f.write(content)

# import json

# books = [{
#   'title': 'Война и мир',
#   'author': 'Лев Толстой',
#   'year' : 1869},
#   {
#   'title': 'Преступление и наказание',
#   'author': 'Федор Достаевский',
#   'year' : 1866}, ]

# with open('data.json', 'w', encoding='utf-8') as json_file:
#   json.dump(books, json_file,
#             ensure_ascii=False,
#             indent=4)


import random

num_count = int(input('Введите количество чисел: '))

numbers = [random.randint(1, 100) for _ in range(num_count)]

with open ('numbers.csv', 'w', encoding='utf-8') as f:
  for number in numbers:
    f.write(f'{number}\n')

from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
operation = input('Операция: ')

with open('log.txt', 'a', encoding='utf-8') as f:
  f.write(f'{timestamp}: {operation}\n')
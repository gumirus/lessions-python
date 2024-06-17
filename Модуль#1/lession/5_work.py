'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 13, 2, 6, 1, 2, 31
c = ['text', 5.5, [True, False], 4]

#Индексация
a = [12, 3, 4]
# 0 1 2
# -3 -2 -1

print(a[2]) #обращаемся к элементу по его индексу
print(a[-2]) #3

a = ['text', 'hello', 'world']
# 1 2
# - 3 -2 -1
print(a[-2])
print(a[2])

#Методы списка

#Создание пустого списка
а = []
#2
а = list()

lst = [4, 2, 10, 100]

lst[3] = 15
print(lst)

#Добавление элемента в конец списка
lst.append('new element')
print(lst)

lst.insert(3, 10000) #a.insrt(x, y) x - номер элемента (index), у - значение
print(lst)

lst.remove(10000) #удаление элемента по значению
print(lst)

#Находим индекс элемента
elem = lst.index('new element')
print(elem)

#Удаляем элемент по индексу
lst.pop(elem)
print(lst)

lst = ['text', 1, 2, 3, 6, True]
print(len(lst))

lst = [1, 3, 2, 6, 5, 4, 9, 11, 10]
lst.sort()
print(lst)

lst.sort()
lst.reverse()
print(lst)

a = [1, 2, 2, 2, 3, 4, 5]
print(a.count(2))

a.clear()
print(a)

a = [1, 2, 2, 2, 3, 4, 5]
print(a)
print(*a)
print(*a, sep=':')

for i in a: #для переменной і в списке а вывести і
  print(i)

spisok = list(map(int, input().split())) 
print(spisok)

lst = [x for x in range(0, 1000)] #Генератор списка
print(lst)

lst = [i ** 2 for i in range(0, 10)]
print(lst)

stroka = 'abcd ef'
# 0123456

print(stroka[-1])

print(stroka[0])

print(stroka[4])


stroka[2] = 'f' 
TypeError: 'str' object does not support item assignment



stroka = 'abcdef'
stroka2 = '123123123'
print(stroka + stroka2)

#Срезы [х:у:z] х - от, у - до, z - с шагом s1 = 'acdeffgasda'
s1 = 'acdeffgasda'
print(s1[3:5])

print(s1[:]) #от начала и до конца

print(s1[::2]) #от начала до конца с шагом 2

print(s1[5:0:-2])

s1 = 'hello world'
print(s1[-1::-1]) #получаем ту же строку с конца

s1 = [2, 3, 4, 5, 6, 7]
print(s1[::2])

s1 = '3 + 8 + 4 + 5 + 6'
t = s1.split(' + ') #Делим строку на элементы по разделителю
print(t)

s1 = ['3', '4', '6', '8'] 
print(' + '.join(s1)) #склеиваем строку по разделителю

a = [ i for i in range(0, 10)]
lst = list()
for i in a:
  if i % 2 == 0:
    lst.append(i)

print(a)
print(lst)
'''
# списки


user = input('Введите ваш e-mail: ')
users =['vanys@ya.ru', 'petya@ya.ru']

if user in users:
  print('Такой пользователь уже зарегистрирован')
else:
  print('Ожидайте сообщение на ваш e-mail')


s1 = 'asdasdasd'
print(s1. upper())

S1 = 'HELLO'
print(s1. lower())

print(ord('a')) #номер символа в таблице
print(chr(97)) #Находим символ по номеру

print(chr (123))

t = 'abzr'
for i in t:
   print(chr(ord (i) + 3))
a = 'text'

а = 'text'
а = 15

''''
1x = 123
Ошибка, название переменной не может начинаться с числа
'''
x = 15
x = 20

#Операторы
a = 10
b = 5

print(a + b) #Сложение
print(a - b) #Вычитание
print(a * b) #Умножение
print(a / b) #Деление



print(7 // 5) #Целочисленное деление
print(7 % 5) #Деление с остатком
print(2 ** 2) #Возведение в степень
print(4 ** 0.5) #Получение квадртного корня из числа через свойсто степеней

#Сокращения

#Вариант 1
a = 5
a = a + 1
print(a)

#Вариант 2
a = 5
a += 1
print(a)

а *= 10
print(a)

a /= 2
print(a)

'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
'''
a, b = map(int, input('Введите числа через пробел: ').split())
print(a * b)

#boolean Логический тип данных
a = True
b = False

# = присваивание а = 5
# == сравнение а == 5, равно ли а числу 5 или нет
a = 10
b = 15
print(a == b) #False
print(a > b) #False
print(a < b) #True
print(a >= b) #False
print(a <= b) #True
print(a != b) #!= неравно

print(a == 5) #True
if a == 5: #Если а == 5, то тогда написать 'а == 5' print('a == 5')
    print(a == 20)#False
if a == 20:
    print('a == 20')

#if если
#elif иначе если
#else иначе

а = 10
if а == 5: #Если а равно числу 5, ко когда print('a == 5') print('a == 5')
    print('a == 5')
else: #иначе print('a != 5')
    print('a != 5')
    print('Блок else')

a = 5
if a == 10: # Если а равно 10, вывести print('а равно 10')
    print('а равно 10')
elif a == 5: #иначе если а равно 5, вывести 'а равно 5"
    print('а равно 5')
else:#если оба условия не верны, то тогда написать...
    print('a не равно 5 или 10')

num1, num2 = map(int, input('Введите 2 числа через пробел:').split())
print('''
+ Сложение
- Вычитание
/ Деление
* Умножение
''')

choice = input('Выберите действие: ')
if choice == '+':
   print(f'{num1} + {num2} = {num1 + num2}')
elif choice == '-':
   print(f'{num1} - {num2} = {num1 - num2}')
elif choice == '*':
   print(f' {num2} = {num1 * num2} *2')
elif choice == '/':
    if num2 == 0:
       print( 'Hа ноль делить нельзя!')
    else:
       print(f' {num1} / {num2} = {num1 / num2}')

а = 9
print(a ** 0.5)

import math #импорт библиотеки

sqrt_a = math.sqrt(a)
print(sqrt_a)

а = 3
print(a ** 5)
pow_a = math.pow(a, 5)
print(pow_a) 
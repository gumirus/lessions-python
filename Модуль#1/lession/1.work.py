
print('привет мир')

print('мой первый код')

a = 15
print(a)

print(10)

name = 'Руслан'
age = '41'
print(name, age)

a = 10 #int integer целое число
b = 5.5 #float число с плавающей точкой (остатком)
c = 'Привет мир!' #str string строка

'''
name = input("Введите ваше имя: ") #input() - ввод данных, принемает str
print (name)

print(type(name) ) #проверяем тип данных переменной nаmе
print(a + b) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
складывать int и str нельзя

a = '15' #str
b = '10' #str
print(a + b)
'''

a = 5 #int
b = 5.5 #float
print(a + b) #10.5

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a + b)

name = input( 'Введите имя:')
year = int(input('Введите год рождения: '))

age = 2024 - year
print(f'Baшe имя:{name}, вам {age} лет!')

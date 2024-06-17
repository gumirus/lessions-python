# тема: Знакомство с условными конструкциями
temp = 10

#(20>) ! else 

if temp > 30:
    print('Жаркая погода')
elif temp >20:
    print('приятная погода')
else:
    print('Прохладно')
    
user_input = int(input('Введите число: '))

if user_input > 0:
    print('Число положительно')
elif user_input < 0:
    print('Число отрицательное')
else:
    print('Число равно нулю')

t_login = 'admin'
t_password = '12345'

login = input('Whire login: ')
password = input('Write password: ')

if login == t_login and password == t_password:
    print('Welcome')
else:
    print('Password or login incorrect')





try: #try
    num1 = int(input('Write number'))
    print('Nothing mistakes')
except:
    print('U wrote not a number')
  

x = 5
y = -2

if x > 0:
    print('x - положительное')
if y < 0:
    print('y - отрицательное')


number = 7

if number %2 == 0:
    print(f'{number} - четное число')
else:
    print(f'{number} - нечетное число')



from random import randint # импортируем рандом (чтобы получить случайные числа)

a = randint(1, 2) # может выпасть либо 1 либо 2
num = randint(1, 2) # 1 or 2

print(f' {num} - num, {a} = a') # выводим значение переменных

if num == 1: # если  num равно 1
  print('Условие 1 выполнено') # выводим условие выполнено
  if a == 1:
     print('Условие 2 выполнено') 
  else:
     print('Условие 2 не выполнено')
else:
  print('Условие 1 не выполнено')

# lower()

a = 'ПРИВЕТ'
print(a.lower())

print('Да' == 'да') # false

if input ('Продолжим?: ').lower() == 'да':
    print('Продолжаем')
else:
    print('Вход')


x = 10

#1 от 10 имеется ввиду от 11 и до 20 (включая 20)
if 10 < x < 20:
    print('Число не находится в диапазоне')
else:
    print('Число назодится в указанном диапазоне')

#2 от 10 до 19

if x in range(10, 20):
    print('Число находится в диапозоне')
else:
    print('Число не находится в указанном диапозоне')
# Программа для кинотеатра
'''
Задание
Напишите программу для кинотеатра. 
Пользователь вводит возраст и наличие сопровождающего. 
Если возраст меньше 12 лет, программа выводит "Билет бесплатный". 
Если возраст от 12 до 18 лет и есть сопровождающий, программа выводит "Билет со скидкой". 
Во всех остальных случаях программа выводит "Полная стоимость билета".
'''
# Запрос возраста пользователя
age = int(input("Введите ваш возраст: "))

# Запрос информации о сопровождающем
accompanying = input("Есть ли у вас сопровождающий? (да/нет): ").lower()

# Проверка условий и вывод соответствующего сообщения
if age < 13:
    print("Билет бесплатный")
elif 12 <= age <= 19 and accompanying == "да":
    print("Билет со скидкой")
else:
    print("Полная стоимость билета")

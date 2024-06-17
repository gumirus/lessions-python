'''
Введение в ООП. Классы и объекты.

Цель: Закрепить на практике работу с классами и объектами, 
научиться самостоятельно писать код в соответствии с парадигмой ООП.

Что нужно сделать: 
Домашнее задание 3

Создайте класс `Car`, который имеет атрибуты 
`make` (марка автомобиля), `model` (модель автомобиля) и 
`year` (год выпуска). Дайте им также метод `display_info()`, 
который выводит информацию о машине (марка, модель и год).

'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

automobile1 = Car('Lada', '2107', 2008)
automobile2 = Car('Mercedes-Benz', 'E-Class', 2020)

automobile1.display_info()
automobile2.display_info()
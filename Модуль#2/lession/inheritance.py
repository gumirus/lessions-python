class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def start_engine(self):
        print('Engine started')

    def drive(self, distance):
        print(f'Driving {distance} kilometers')


class ElectricCar(Car):
    def __init__(self, brand, model, color, year, battery_capacity):
        super().__init__(brand, model, color, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print('Charging')

    def drive(self, distance):
        super().drive(distance)
        print(f'Battery remains: {self.battery_capacity - distance}')


car1 = Car('Honda', 'Civic', 'Red', 2024)
car1.drive(100)
car1.start_engine()

ecar = ElectricCar('Super', 'New', 'White', 2024, 10000)
ecar.start_engine()
ecar.charge()
ecar.drive(500)

#---------------------------------------------------------------------------

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def purr(self):
        print(f'{self.name} the cat is purring')


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f'{self.name} the dog is barking')


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.name} the bird is flying')

    def sleep(self):  # Добавлен метод sleep для класса Bird
        print(f'{self.name} the bird is sleeping')


# Создание объектов и вызов методов
cat = Cat('Whiskers', 2, 'black')
dog = Dog('Buddy', 3, 'Labrador')
bird = Bird('Tweety', 1, 30)

print("--- Animals ---")
cat.eat()
dog.eat()
bird.eat()

print("--- Sleeping ---")
cat.sleep()
dog.sleep()
bird.sleep()

print("--- Actions ---")
dog.bark()
bird.fly()

#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# Определение классов Person, Student, Teacher и Employee
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} I'm a student with ID: {self.student_id}"

    def learn(self):
        return f"Student {self.name} is learning"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} I teach {self.subject}"
    
    def teach(self):
        return f"{self.name} is teaching {self.subject}"
    

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def introduce(self):
        return f"{super().introduce()} I work as a {self.position}."

    def work(self):
        return f"{self.name} is working"

# Создание объектов и вызов методов
student = Student('Alice', 15, '123123123')
teacher = Teacher('Mr. Smith', 50, 'Math')
employee = Employee('John', 30, 'Engineer')

print(student.introduce())
print(student.learn())

print(teacher.introduce())
print(teacher.teach())

print(employee.introduce())
print(employee.work())

# Определение классов App и CustomApp для Tkinter
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Basic App')
        self.geometry('300x200')

        self.label = tk.Label(self, text='Hello, World!')
        self.label.pack(pady=20)

        self.button = tk.Button(self, text='Click me', 
                                command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        messagebox.showinfo('Info', 'Base APP')


class CustomApp(App):
    def __init__(self):
        super().__init__()
        self.title('Custom App')

        self.custom_button = tk.Button(self, text='Custom Button', 
                                       command=self.on_custom_button_click)
        self.custom_button.pack(pady=10)

    def on_custom_button_click(self):
        messagebox.showinfo('Info', 'Custom APP')


# Создание и запуск одного экземпляра приложения
if __name__ == '__main__':
    # Для запуска базового приложения используйте следующую строку
    # app = App()

    # Для запуска пользовательского приложения используйте следующую строку
    app = CustomApp()
    app.mainloop()

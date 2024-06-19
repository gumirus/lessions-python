class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('The animal is eating')

    def sleep(self):
        print('The animal is sleeping')

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def purr(self):
        print('The cat is purring')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print('The dog is barking')

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print('The bird is flying')


cat = Cat('Whiskers', 5, 'Gray')
dog = Dog('Buddy', 3, 'Labrador')
bird = Bird('Tweety', 1, 20)

cat.eat()
dog.eat()
bird.sleep()

cat.purr()
dog.bark()
bird.fly()

#---------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Basic App')
        self.geometry('300x200')

        self.label = tk.Label(self, text='Hello, World!')
        self.label.pack(pady=20)

        self.button = tk.Button(self, text='Click me', command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        messagebox.showinfo('Info', 'Base APP')

class CustomApp(App):
    def __init__(self):
        super().__init__()
        self.title('Custom App')    
        self.custom_button = tk.Button(self, text='Custom Button', command=self.on_custom_button_click)
        self.custom_button.pack(pady=10)

    def on_custom_button_click(self):
        messagebox.showinfo('Info', 'Custom APP')

if __name__ == '__main__':
    app = CustomApp()
    app.mainloop()

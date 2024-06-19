'''
Наследование в классах, создание собственных объектов.

Домашнее задание 4

Создайте родительский класс `Animal` 
с атрибутами `name` и `species`.
Дайте им также метод `make_sound()`, 
который выводит звук, издаваемый животными.


Создайте подклассы `Dog` и `Cat`, 
которые наследуют от класса `Animal`. 
Дайте каждому из них свой собственный метод `make_sound()`, 
который выводит соответствующий звук 
(`"Гав"` для собаки и `"Мяу"` для кота).

'''

import tkinter as tk
import pygame
import os

class Animal:
    def __init__(self, name, species, sound_file):
        self.name = name
        self.species = species
        self.sound_file = sound_file

    def make_sound(self):
        pygame.mixer.init()
        if os.path.exists(self.sound_file):
            sound = pygame.mixer.Sound(self.sound_file)
            sound.play()
        else:
            print(f"Файл '{self.sound_file}' не найден!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'Dog', 'dog.mp3')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Cat', 'cat.mp3')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Animal Sounds')
        self.geometry('300x200')

        self.label = tk.Label(self, text='Click the buttons to hear animal sounds!')
        self.label.pack(pady=20)

        self.dog_button = tk.Button(self, text='Dog Sound', command=self.play_dog_sound)
        self.dog_button.pack(pady=10)

        self.cat_button = tk.Button(self, text='Cat Sound', command=self.play_cat_sound)
        self.cat_button.pack(pady=10)

    def play_dog_sound(self):
        dog = Dog('Buddy')
        dog.make_sound()

    def play_cat_sound(self):
        cat = Cat('Whiskers')
        cat.make_sound()

if __name__ == '__main__':
    app = App()
    app.mainloop()

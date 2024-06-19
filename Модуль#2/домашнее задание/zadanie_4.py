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

#--------------------------------------------------------------------------------------------

'''
import tkinter as tk
import pygame
import os

tkinter - библиотека для создания графических интерфейсов в Python.
pygame - библиотека для работы с мультимедиа, в частности для воспроизведения звуков.
os - модуль для работы с файловой системой, используется для проверки наличия файлов

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

__init__ - конструктор класса, инициализирует атрибуты name (имя животного), 
species (вид животного), sound_file (путь к звуковому файлу).
make_sound - метод для воспроизведения звука:
Инициализирует модуль микшера pygame.
Проверяет наличие звукового файла с помощью os.path.exists.
Если файл существует, загружает и воспроизводит его с помощью pygame.mixer.Sound.
Если файл не найден, выводит сообщение об ошибке.

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'Dog', 'dog.mp3')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Cat', 'cat.mp3')

Dog и Cat - подклассы класса Animal.
Конструкторы этих классов вызывают конструктор родительского класса Animal 
с фиксированным значением для species и sound_file:
Dog передает 'Dog' и 'dog.mp3'.
Cat передает 'Cat' и 'cat.mp3'

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

App - класс, наследующий от tk.Tk, основного класса для создания главного окна в Tkinter.
__init__ - конструктор класса, инициализирует графический интерфейс:
Устанавливает заголовок окна и его размер.
Создает и размещает метку label с текстом.
Создает две кнопки: одну для воспроизведения звука собаки и другую для звука кота.
Каждая кнопка вызывает соответствующий метод (play_dog_sound или play_cat_sound) при нажатии.
play_dog_sound и play_cat_sound - методы, которые создают объекты Dog и Cat соответственно и 
вызывают их метод make_sound

if __name__ == '__main__':
    app = App()
    app.mainloop()

Этот блок кода проверяет, что скрипт выполняется напрямую, а не импортируется как модуль.
Создается экземпляр класса App и запускается основной цикл Tkinter с app.mainloop().

Как работает код

1)Импортируются необходимые библиотеки.

2)Определяются классы Animal, Dog, и Cat.

3)Определяется класс App для графического интерфейса.

4)При запуске программы создается и отображается окно Tkinter с двумя кнопками.

5)При нажатии на кнопку создается соответствующий объект (собака или кот) и воспроизводится звук, 
если звуковой файл найден.
'''
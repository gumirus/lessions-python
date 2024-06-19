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

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Животное издает звук")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Собака")

    def make_sound(self):
        print("Гав")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Кот")

    def make_sound(self):
        print("Мяу")

dog1 = Dog("Дунай")
cat1 = Cat("Мурка")


dog1.make_sound()
cat1.make_sound()

# import tkinter as tk
# from tkinter import messagebox
# # import simpleaudio as sa

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         pass  # Абстрактный метод, будет переопределён в подклассах


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Dog')

#     def make_sound(self):
#         wave_obj = sa.WaveObject.from_wave_file('dog.wav')
#         wave_obj.play()


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Cat')

#     def make_sound(self):
#         wave_obj = sa.WaveObject.from_wave_file('cat.wav')
#         wave_obj.play()


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Animal Sounds')
#         self.geometry('300x200')

#         self.label = tk.Label(self, text='Click the buttons to hear animal sounds!')
#         self.label.pack(pady=20)

#         self.dog_button = tk.Button(self, text='Dog Sound', command=self.play_dog_sound)
#         self.dog_button.pack(pady=10)

#         self.cat_button = tk.Button(self, text='Cat Sound', command=self.play_cat_sound)
#         self.cat_button.pack(pady=10)

#     def play_dog_sound(self):
#         dog = Dog('Buddy')
#         dog.make_sound()

#     def play_cat_sound(self):
#         cat = Cat('Whiskers')
#         cat.make_sound()


# # Создание и запуск одного экземпляра приложения
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import pygame

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         pass  # Abstract method, to be overridden in subclasses


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Dog')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound('dog.wav')
#         sound.play()


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Cat')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound('cat.wav')
#         sound.play()


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Animal Sounds')
#         self.geometry('300x200')

#         self.label = tk.Label(self, text='Click the buttons to hear animal sounds!')
#         self.label.pack(pady=20)

#         self.dog_button = tk.Button(self, text='Dog Sound', command=self.play_dog_sound)
#         self.dog_button.pack(pady=10)

#         self.cat_button = tk.Button(self, text='Cat Sound', command=self.play_cat_sound)
#         self.cat_button.pack(pady=10)

#     def play_dog_sound(self):
#         dog = Dog('Buddy')
#         dog.make_sound()

#     def play_cat_sound(self):
#         cat = Cat('Whiskers')
#         cat.make_sound()


# # Create and run a single instance of the application
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import pygame
# import os

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         pass  # Абстрактный метод, должен быть переопределен в подклассах

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Dog')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound_file = 'dog.mp3'
#         if os.path.exists(sound_file):
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#         else:
#             print(f"Файл '{sound_file}' не найден!")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Cat')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound_file = 'cat.mp3'
#         if os.path.exists(sound_file):
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#         else:
#             print(f"Файл '{sound_file}' не найден!")

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Animal Sounds')
#         self.geometry('300x200')

#         self.label = tk.Label(self, text='Нажмите на кнопки, чтобы услышать звуки животных!')
#         self.label.pack(pady=20)

#         self.dog_button = tk.Button(self, text='Звук собаки', command=self.play_dog_sound)
#         self.dog_button.pack(pady=10)

#         self.cat_button = tk.Button(self, text='Звук кошки', command=self.play_cat_sound)
#         self.cat_button.pack(pady=10)

#     def play_dog_sound(self):
#         dog = Dog('Buddy')
#         dog.make_sound()

#     def play_cat_sound(self):
#         cat = Cat('Whiskers')
#         cat.make_sound()

# # Создание и запуск единственного экземпляра приложения
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Dog')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound_file = 'C:/Users/agori/.vscode/projects/lessions-python/dog.mp3'
#         if os.path.exists(sound_file):
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#         else:
#             print(f"Файл '{sound_file}' не найден!")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'Cat')

#     def make_sound(self):
#         pygame.mixer.init()
#         sound_file = 'C:/Users/agori/.vscode/projects/lessions-python/cat.mp3'
#         if os.path.exists(sound_file):
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#         else:
#             print(f"Файл '{sound_file}' не найден!")


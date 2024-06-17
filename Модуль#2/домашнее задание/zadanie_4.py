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

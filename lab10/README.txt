Клас Student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
Опис: Цей клас представляє студента з ім'ям, віком і оцінкою. 
Клас має конструктор __init__, який ініціалізує атрибути name, age і grade. Метод display_info повертає рядок із інформацією про студента.

Клас Animal

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"

Опис: Базовий клас Animal з атрибутами name і sound, який представляє тварину з іменем і звуком, який вона видає. Метод make_sound повертає рядок із звуком тварини.

Клас Dog

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

Опис: Клас, що успадковується від Animal, що представляє собаку зі звуком і породою.
Використовує метод __init__ батьківського класу через super() для ініціалізації атрибутів і додає власний атрибут breed.

Класи Bird, Sparrow, Penguin

class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

Опис: Клас Bird є базовим класом для птахів і має метод fly, який відсутній. 
Класи Sparrow і Penguin успадковують клас Bird і перевизначають метод fly, повертаючи різні значення в залежності від типу птаха.

Клас Encapsulation

class Encapsulation:
    def __init__(self, public, private, protected):
        self.public = public
        self._private = private
        self.__protected = protected

Опис: Клас, що демонструє інкапсуляцію. Має атрибути public, _private (закритий атрибут) і __protected (захищений атрибут).

Клас Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

Опис: Клас, що представляє прямокутник з шириною і висотою. Має метод calculate_perimeter, який обчислює периметр прямокутника.

Клас AverageCalculator

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

Опис: Клас, що обчислює середнє значення чисел. Ініціалізується списком чисел, має метод calculate_average, який повертає середнє значення цих чисел.
Кожен з цих класів виконує свої функції і показує основні концепції об'єктно-орієнтованого програмування, такі як успадкування, інкапсуляція, поліморфізм та інші.
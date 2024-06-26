Звіт по Python-коду

Наведений код включає десять функцій (task1 до task10), кожна з яких виконує різні обчислювальні завдання з числами, списками і рядками. Ось докладний опис кожної функції:
    Призначення: Повертає найбільше з трьох чисел.
    Вхідні дані:
        a, b, c (тип int або float): Числа для порівняння.
    Вихідні дані:
        Найбільше число (тип int або float).

Докладний опис:
Функція task1 приймає три числа a, b і c і використовує вбудовану функцію max() для знаходження найбільшого числа серед них.
Приклад використання:

result = task1(10, 5, 20)
print(result)  # Виведе: 20

2. Функція task2
    Призначення: Обчислює суму всіх елементів у списку.
    Вхідні дані:
        list (тип list): Список чисел для сумування.
    Вихідні дані:
        Сума всіх елементів списку (тип int або float).

Докладний опис:
Функція task2 використовує вбудовану функцію sum() для обчислення суми всіх елементів у вхідному списку чисел.

Приклад використання:

result = task2([1, 2, 3, 4, 5])
print(result)  # Виведе: 15

3. Функція task3

    Призначення: Обчислює добуток всіх елементів у списку чисел.
    Вхідні дані:
        list (тип list): Список чисел для множення.
    Вихідні дані:
        Добуток всіх елементів списку (тип int або float).

Докладний опис:
Функція task3 проходить по кожному елементу у списку list і множить їх між собою, починаючи з початкового значення 1.

Приклад використання:

result = task3([1, 2, 3, 4])
print(result)  # Виведе: 24

4. Функція task4

    Призначення: Повертає рядок, записаний у зворотньому порядку.
    Вхідні дані:
        str (тип str): Рядок для обертання.
    Вихідні дані:
        Рядок, записаний у зворотньому порядку (тип str).

Докладний опис:
Функція task4 використовує зріз рядка [::1], щоб повернути рядок у зворотньому порядку.

Приклад використання:

result = task4("hello")
print(result)  # Виведе: "olleh"

5. Функція task5

    Призначення: Обчислює факторіал числа a.
    Вхідні дані:
        a (тип int): Число для обчислення факторіалу.
    Вихідні дані:
        Факторіал числа a (тип int або float).

Докладний опис:
Функція task5 обчислює факторіал числа a, тобто добуток усіх цілих чисел від 1 до a.

Приклад використання:

result = task5(5)
print(result)  # Виведе: 120

6. Функція task6

    Призначення: Перевіряє, чи число a належить діапазону від 25 до 50 включно.
    Вхідні дані:
        a (тип int або float): Число для перевірки.
    Вихідні дані:
        Логічне значення (True або False).

Докладний опис:
Функція task6 використовує оператор порівняння для перевірки, чи число a знаходиться у вказаному діапазоні.

Приклад використання:

result = task6(30)
print(result)  # Виведе: True

7. Функція task7

    Призначення: Підраховує кількість великих і малих літер у рядку.
    Вхідні дані:
        str (тип str): Рядок для аналізу.
    Вихідні дані:
        Кількість великих і малих літер (тип int, int).

Докладний опис:
Функція task7 використовує методи isupper() і islower() для підрахунку великих і малих літер у вхідному рядку str.

Приклад використання:

upper, lower = task7("Hello World")
print(upper, lower)  # Виведе: 2 8

Звіт по Python-коду

Наведений код включає десять функцій (task1 до task10), кожна з яких виконує різні обчислювальні завдання з числами, списками і рядками. Ось докладний опис кожної функції:
1. Функція task1

python

def task1(a, b, c):
    return max(a, b, c)

    Призначення: Повертає найбільше з трьох чисел.
    Вхідні дані:
        a, b, c (тип int або float): Числа для порівняння.
    Вихідні дані:
        Найбільше число (тип int або float).

Докладний опис:
Функція task1 приймає три числа a, b і c і використовує вбудовану функцію max() для знаходження найбільшого числа серед них.

Приклад використання:

python

result = task1(10, 5, 20)
print(result)  # Виведе: 20

2. Функція task2

python

def task2(list):
    return sum(list)

    Призначення: Обчислює суму всіх елементів у списку.
    Вхідні дані:
        list (тип list): Список чисел для сумування.
    Вихідні дані:
        Сума всіх елементів списку (тип int або float).

Докладний опис:
Функція task2 використовує вбудовану функцію sum() для обчислення суми всіх елементів у вхідному списку чисел.

Приклад використання:

python

result = task2([1, 2, 3, 4, 5])
print(result)  # Виведе: 15

3. Функція task3

python

def task3(list):
    result = 1
    for i in list:
        result *= i
    return result

    Призначення: Обчислює добуток всіх елементів у списку чисел.
    Вхідні дані:
        list (тип list): Список чисел для множення.
    Вихідні дані:
        Добуток всіх елементів списку (тип int або float).

Докладний опис:
Функція task3 проходить по кожному елементу у списку list і множить їх між собою, починаючи з початкового значення 1.

Приклад використання:

python

result = task3([1, 2, 3, 4])
print(result)  # Виведе: 24

4. Функція task4

python

def task4(str):
    return str[::-1]

    Призначення: Повертає рядок, записаний у зворотньому порядку.
    Вхідні дані:
        str (тип str): Рядок для обертання.
    Вихідні дані:
        Рядок, записаний у зворотньому порядку (тип str).

Докладний опис:
Функція task4 використовує зріз рядка [::1], щоб повернути рядок у зворотньому порядку.

Приклад використання:

python

result = task4("hello")
print(result)  # Виведе: "olleh"

5. Функція task5

python

def task5(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

    Призначення: Обчислює факторіал числа a.
    Вхідні дані:
        a (тип int): Число для обчислення факторіалу.
    Вихідні дані:
        Факторіал числа a (тип int або float).

Докладний опис:
Функція task5 обчислює факторіал числа a, тобто добуток усіх цілих чисел від 1 до a.

Приклад використання:

python

result = task5(5)
print(result)  # Виведе: 120

6. Функція task6

python

def task6(a):
    return 25 <= a <= 50

    Призначення: Перевіряє, чи число a належить діапазону від 25 до 50 включно.
    Вхідні дані:
        a (тип int або float): Число для перевірки.
    Вихідні дані:
        Логічне значення (True або False).

Докладний опис:
Функція task6 використовує оператор порівняння для перевірки, чи число a знаходиться у вказаному діапазоні.

Приклад використання:

python

result = task6(30)
print(result)  # Виведе: True

7. Функція task7

python

def task7(str):
    upper_count = sum(1 for char in str if char.isupper())
    lower_count = sum(1 for char in str if char.islower())
    return upper_count, lower_count

    Призначення: Підраховує кількість великих і малих літер у рядку.
    Вхідні дані:
        str (тип str): Рядок для аналізу.
    Вихідні дані:
        Кількість великих і малих літер (тип int, int).

Докладний опис:
Функція task7 використовує методи isupper() і islower() для підрахунку великих і малих літер у вхідному рядку str.

Приклад використання:

python

upper, lower = task7("Hello World")
print(upper, lower)  # Виведе: 2 8

8. Функція task8

    Призначення: Видаляє дублікати зі списку.
    Вхідні дані:
        list1 (тип list): Список з можливими дублікатами.
    Вихідні дані:
        Новий список без дублікатів (тип list).

Докладний опис:
Функція task8 використовує структуру set, яка автоматично видаляє дублікати, а потім перетворює його назад у список.

Приклад використання:

result = task8([1, 2, 2, 3, 4, 4, 5])
print(result)  # Виведе: [1, 2, 3, 4, 5]

9. Функція task9

    Призначення: Вибирає всі парні числа зі списку.
    Вхідні дані:
        list (тип list): Список чисел для фільтрації.
    Вихідні дані:
        Новий список з парними числами (тип list).

Докладний опис:
Функція task9 використовує умовну генерацію списку для відбору парних чисел із вхідного списку list.

Приклад використання:

result = task9([1, 2, 3, 4, 5, 6])
print(result)  # Виведе: [2, 4, 6]

10. Функція task10

    Призначення: Обчислює найбільше число в останньому ряду трикутника Паскаля.
    Вхідні дані:
        n (тип int): Індекс ряду трикутника Паскаля.
    Вихідні дані:
        Найбільше число в останньому ряду трикутника Паскаля (тип int або float).

Докладний опис:
Функція task10 використовує внутрішню функцію calculate_pascal_triangle_row, щоб обчислити n-ий ряд трикутника Паскаля і повертає найбільший елемент у цьому ряді.

Приклад використання:

result = task10(4)
print(result)  # Виведе: 6
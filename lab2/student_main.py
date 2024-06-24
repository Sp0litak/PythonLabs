def task1(number1, operator, number2):
    if operator == '>':
        return number1 > number2
    elif operator == '<':
        return number1 < number2
    elif operator == '>=':
        return number1 >= number2
    elif operator == '<=':
        return number1 <= number2
    elif operator == '==':
        return number1 == number2
    elif operator == '!=':
        return number1 != number2


def task2(text, number):
    length_of_text = len(text)
    return max(length_of_text, number)


def task3(number1, number2, number3):
    return number1 == number2 == number3



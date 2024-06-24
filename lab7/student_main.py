def task1(age):
    try:
        age = int(age)
        return age
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

def task2(num1, num2):
    try:
        product = int(num1) * int(num2)
        return product
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."

def task3(input_str):
    if isinstance(input_str, str):
        return len(input_str)
    else:
        return "Error: Please enter a string, not a numeric value."

def task4(int_list):
    try:
        if all(isinstance(x, int) for x in int_list):
            return sum(int_list)
        else:
            return None
    except TypeError:
        return None

def task5(data):
    result = []
    try:
        for name, grades in data:
            avg_grade = sum(grades) / len(grades)
            result.append((avg_grade, name))
        return result
    except Exception:
        return "List processing error!"
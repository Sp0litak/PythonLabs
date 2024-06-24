def task1(a,b,c):
    return max(a,b,c)

def task2(list):
    return sum(list)

def task3(list):
    result = 1
    for i in list:
        result *= i
    return result

def task4(str):
    return str[::-1]

def task5(a):
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

def task6(a):
    return 25 <= a <= 50

def task7(str):
    upper_count = sum(1 for char in str if char.isupper())
    lower_count = sum(1 for char in str if char.islower())
    return upper_count, lower_count

def task8(list1):
    return list(set(list1))

def task9(list):
    return [num for num in list if num % 2 == 0]

def task10(n):
    def calculate_pascal_triangle_row(row_index):
        row = [1]
        for i in range(1, row_index + 1):
            row.append(row[i - 1] * (row_index - i + 1) // i)
        return row

    last_row = calculate_pascal_triangle_row(n)
    return max(last_row)
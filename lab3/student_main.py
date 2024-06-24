def task1(my_list):
    my_list.insert(1, -5)

    min_element = min(my_list)
    max_element = max(my_list)

    my_list.insert(2, [1, 2, 3])


    my_list.append(["Прізвище", "Ім'я"])

    list_length = len(my_list)

    print(f"Список після змін: {my_list}")
    print(f"Мінімальний елемент: {min_element}")
    print(f"Максимальний елемент: {max_element}")
    print(f"Довжина списку: {list_length}")

    return my_list, min_element, max_element, list_length


def task2(A, B, C):
    total_cost = 0
    for i in range(len(A)):
        total_cost += B[i] * C[i]

    average_price = sum(C) / len(C)

    most_stocked_item_index = B.index(max(B))
    most_stocked_item = A[most_stocked_item_index]

    return total_cost, average_price, most_stocked_item

def task3():

    import random
    numbers = [random.randint(-25, 25) for _ in range(50)]

    A1 = [num for num in numbers if num > 0]

    A2 = [num for num in numbers if num < 0]

    return A1, A2


def task4(my_string):
    count_a = my_string.lower().count('a')

    return count_a

def task5(my_string):
    modified_str = my_string.replace('GOOD', 'NICE')

    words = modified_str.split()
    word_count = len(words)

    return modified_str, word_count

def task6():
    total_sum = sum(range(1, 6))
    return total_sum

def task7(my_list):
    result = [num for num in my_list if num % 7 == 0 and num % 5 == 0]

    return result

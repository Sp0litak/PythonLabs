1. Генератори числових послідовностей:

    number_generator(numbers):
        Генерує числа зі списку.

    even_number_generator(start, end):
        Генерує парні числа у заданому діапазоні.

    odd_number_generator(start, end):
        Генерує непарні числа у заданому діапазоні.

    fibonacci_generator():
        Генерує числа Фібоначчі безкінечно.

    prime_number_generator(limit):
        Генерує прості числа до заданого ліміту.

2. Генератори для обходу бінарних дерев та графів:

    pre_order_traversal(root):
        Попередній обхід бінарного дерева.

    in_order_traversal(root):
        Центральний обхід бінарного дерева.

    post_order_traversal(root):
        Зворотній обхід бінарного дерева.

    dfs_traversal(graph, start):
        Пошук в глибину в графі.

    bfs_traversal(graph, start):
        Пошук в ширину в графі.

3. Генератори для роботи зі словниками та файлами:

    dict_keys_generator(dictionary):
        Генерує ключі словника.

    dict_values_generator(dictionary):
        Генерує значення словника.

    dict_items_generator(dictionary):
        Генерує пари (ключ, значення) словника.

    file_lines_generator(file_path):
        Генерує рядки з файлу.

    file_words_generator(file_path):
        Генерує слова з файлу.

4. Інші генератори:

    string_chars_generator(input_string):
        Генерує символи зі строки.

    unique_elements_generator(input_list):
        Генерує унікальні елементи зі списку.

    reverse_list_generator(input_list):
        Генерує елементи списку у зворотньому порядку.

    cartesian_product_generator(list1, list2):
        Генерує декартовий добуток двох списків.

    permutations_generator(input_list):
        Генерує всі перестановки списку.

    combinations_generator(input_list):
        Генерує всі комбінації елементів списку.

    tuple_list_generator(tuple_list):
        Генерує елементи зі списку кортежів.

    parallel_lists_generator(*lists):
        Генерує елементи з декількох списків паралельно.

    flatten_list_generator(nested_list):
        Генерує елементи з вкладеного списку.

    nested_dict_generator(nested_dict):
        Генерує елементи з вкладеного словника.

    powers_of_two_generator(n):
        Генерує степені числа 2 до певного числа.

    powers_of_base_generator(base, limit):
        Генерує степені заданого числа до певного ліміту.

    squares_generator(start, end):
        Генерує квадрати чисел у заданому діапазоні.

    cubes_generator(start, end):
        Генерує куби чисел у заданому діапазоні.

    factorials_generator(n):
        Генерує факторіали чисел до певного числа.

    collatz_sequence_generator(n):
        Генерує послідовність Коллатца для заданого числа.

    geometric_progression_generator(initial, ratio, limit):
        Генерує геометричну прогресію.

    arithmetic_progression_generator(initial, difference, limit):
        Генерує арифметичну прогресію.

    running_sum_generator(numbers):
        Генерує накопичувальну суму чисел.

    running_product_generator(numbers):
        Генерує накопичувальний добуток чисел.

Ці генератори дозволяють ефективно обробляти дані та отримувати послідовності значень без потреби зберігати всі елементи у пам'яті одразу.
\ Вони корисні для ітерації через великі обсяги даних або для генерації безкінечних послідовностей, як от чисел Фібоначчі або простих чисел.
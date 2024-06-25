1. Функція task1: Сума квадратів елементів масиву

Призначення: Обчислює суму квадратів елементів вхідного масиву.

Код:

def task1(arr):
    return sum(x ** 2 for x in arr)

Приклад використання:

task1([1, 2, 3, 4])  # Повертає 30

2. Функція task2: Сума елементів, що перевищують середнє значення

Призначення: Обчислює суму елементів, які більші за середнє значення масиву.

Код:

def task2(arr):
    average = sum(arr) / len(arr)
    return sum(x for x in arr if x > average)

Приклад використання:


task2([1, 2, 3, 4, 5])  # Повертає 9

3. Функція task3: Сортування за частотою та значенням

Призначення: Сортує масив за спаданням частоти елементів. Якщо частоти однакові, сортує за зростанням значення.

Код:


def task3(arr):
    counts = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-counts[x], x))
    return sorted_arr

Приклад використання:


task3([4, 4, 2, 2, 2, 3, 1])  # Повертає [2, 2, 2, 4, 4, 1, 3]

4. Функція task4: Пошук пропущеного числа в послідовності

Призначення: Знаходить пропущене число в послідовності від 1 до n.

Код:


def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

Приклад використання:

task4([1, 2, 4, 5, 6])  # Повертає 3

5. Функція task5: Найдовша послідовність чисел

Призначення: Знаходить довжину найдовшої послідовності підрядних чисел.

Код:

def task5(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

Приклад використання:


task5([100, 4, 200, 1, 3, 2])  # Повертає 4

6. Функція task6: Поворот масиву на k елементів

Призначення: Повертає масив на k елементів праворуч.

Код:


def task6(arr, k):
    k %= len(arr)
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr

Приклад використання:


task6([1, 2, 3, 4, 5, 6, 7], 3)  # Повертає [5, 6, 7, 1, 2, 3, 4]

7. Функція task7: Добуток елементів масиву, за винятком поточного

Призначення: Повертає масив, де кожен елемент є добутком всіх інших елементів вхідного масиву, за винятком поточного.

Код:


def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

Приклад використання:


task7([1, 2, 3, 4])  # Повертає [24, 12, 8, 6]

8. Функція task8: Максимальна сума підмасиву

Призначення: Знаходить максимальну суму підмасиву в даному масиві чисел.

Код:


def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

Приклад використання:


task8([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # Повертає 6

9. Функція task9: Спіральний обхід матриці

Призначення: Повертає елементи матриці в порядку спірального обходу.

Код:

def task9(matrix):
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

Приклад використання:

task9([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])  # Повертає [1, 2, 3, 6, 9, 8, 7, 4, 5]

10. Функція task10: Найближчі точки до початку координат

Призначення: Знаходить k найближчих точок до початку координат.

Код:

def task10(points, k):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    heap = [(distance(point), point) for point in points]
    heapq.heapify(heap)

    closest_points = [heapq.heappop(heap)[1] for _ in range(k)]

    return closest_points

Приклад використання:

task10([(1, 3), (3, 4), (2, -1)], 2)  # Повертає [(1, 3), (2, -1)]
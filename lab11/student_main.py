from collections import Counter # task 3
import heapq # task 10


def task1(arr):
    return sum(x ** 2 for x in arr)

def task2(arr):
    average = sum(arr) / len(arr)
    return sum(x for x in arr if x > average)

def task3(arr):
    counts = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-counts[x], x))
    return sorted_arr

def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number


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

def task6(arr, k):
    k %= len(arr)
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr


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


def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

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


def task10(points, k):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    heap = [(distance(point), point) for point in points]
    heapq.heapify(heap)

    closest_points = [heapq.heappop(heap)[1] for _ in range(k)]

    return closest_points
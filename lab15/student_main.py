import re


# Task 1: Clean Data
def clean_data(data):
    cleaned = list(map(lambda x: x.strip().lower(), data.split(',')))
    return cleaned


# Task 2: Filter Emails
def filter_emails(emails):
    def is_valid_email(email):
        return '@' in email and email.count('@') == 1

    valid_emails = list(filter(is_valid_email, map(str.strip, emails.split())))
    return valid_emails


# Task 3: Extract Keywords
def extract_keywords(words, length):
    filtered_words = list(filter(lambda word: len(word) > length, map(str.strip, words.split())))
    return filtered_words


# Task 4: Process Text Data
def process_text(texts):
    processed_texts = list(
        filter(lambda x: len(x) > 1, map(lambda x: re.sub(r'\W+', '', x.strip().lower()), texts.split(','))))
    return processed_texts


# Task 5: Normalize Data
def normalize_data(numbers):
    max_value = max(map(float, numbers.split(',')))
    normalized_numbers = list(map(lambda x: float(x) / max_value, numbers.split(',')))
    return normalized_numbers


# Task 6: Concatenate Strings
def concatenate_strings(data, separator):
    concatenated = ''.join(data.split(separator))
    return concatenated


# Task 7: Sum Numeric Strings
def sum_numeric_strings(numbers):
    def is_numeric(s):
        return s.replace('.', '', 1).isdigit()

    numeric_values = map(float, filter(is_numeric, numbers.split(',')))
    total_sum = sum(numeric_values)
    return total_sum


# Task 8: Filter Numbers
def filter_numbers(numbers, threshold):
    def is_above_threshold(s):
        try:
            num = float(s)
            return num > threshold
        except ValueError:
            return False

    filtered = list(filter(is_above_threshold, numbers.split()))
    return filtered


# Task 9: Map to Squares
def map_to_squares(numbers):
    squared_numbers = list(map(lambda x: int(x) ** 2, numbers.split(',')))
    return squared_numbers


# Task 10: Reverse Strings
def reverse_strings(words):
    reversed_words = list(map(lambda x: x[::-1], words.split(',')))
    return reversed_words
import re

def task1(input_str):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, input_str))

def task2(input_str):
    pattern = r'[A-Z]'
    return bool(re.search(pattern, input_str))

def task3(input_str):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, input_str))

def task4(input_str):
    pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, input_str))

def task5(input_str):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, input_str))

def task6(input_str):
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, input_str))

def task7(input_str):
    pattern = r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    return bool(re.match(pattern, input_str))

def task8(input_str):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, input_str))

def task9(input_str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(pattern, input_str))

def task10(input_str):
    pattern = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'
    return bool(re.match(pattern, input_str))
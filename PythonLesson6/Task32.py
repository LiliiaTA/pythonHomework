# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

def indices_in_range(arr, min_val, max_val):
    result = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            result.append((i, arr[i]))
    return result

# Пример использования:
arr = [1, 3, 7, 10, 5, 8]
min_val = 4
max_val = 8
result = indices_in_range(arr, min_val, max_val)
print(', '.join([f'{i}({v})' for i, v in result]))
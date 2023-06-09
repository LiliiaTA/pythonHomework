# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

n = int(input("Введите количество элементов в массиве: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))
x = int(input("Введите число X: "))

min_diff = float("inf")
closest_num = None

for i in range(n):
    diff = abs(a[i] - x)
    if diff < min_diff:
        min_diff = diff
        closest_num = a[i]

print("Самый близкий по величине элемент в массиве к числу", x, "равен", closest_num)
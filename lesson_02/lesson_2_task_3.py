import math


def square(items):
    return math.ceil(items * items)


num_items = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(num_items)}")

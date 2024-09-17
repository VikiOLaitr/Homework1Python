import math

def square(items):
    return math.ceil(items * items)

num_items = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(num_items)}")
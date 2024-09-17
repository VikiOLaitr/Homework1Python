n = int(input("Введите число:"))
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"FizzBuzz")
        elif i % 5 == 0:
            print(f"Buzz")
        elif i % 3 == 0:
            print(f"Fizz")
        else:
            print(i)
fizz_buzz(n)
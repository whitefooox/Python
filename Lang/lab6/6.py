def square_fibonacci(n):
    first = 1
    second = 0
    for _ in range(n):
        first, second = second, first + second
        yield second ** 2

print(list(square_fibonacci(7)))
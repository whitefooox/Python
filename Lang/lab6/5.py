def factorials(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x

print(list(factorials(7)))

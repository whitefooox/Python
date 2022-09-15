def power(a, n):
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)

print(power(2, 10))
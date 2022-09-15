def power(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res

print(power(int(input()), int(input())))
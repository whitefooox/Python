number = int(input())

x1 = number // 1000
x2 = number // 100 % 10
x3 = number // 10 % 10
x4 = number % 10

if x1 > x2:
    x1, x2 = x2, x1
if x2 > x3:
    x2, x3 = x3, x2
if x3 > x4:
    x3, x4 = x4, x3
if x1 > x2:
    x1, x2 = x2, x1
if x2 > x3:
    x2, x3 = x3, x2
if x1 > x2:
    x1, x2 = x2, x1
if x1 == 0 and x2:
    x1, x2 = x2, x1
elif x1 == 0 and x3:
    x1, x3 = x3, x1
elif x1 == 0 and x4:
    x1, x4 = x4, x1

print(x4 + 10 * (x3 + 10 * (x2 + 10 * x1)))

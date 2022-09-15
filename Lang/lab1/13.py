n = int(input())
m = int(input())
symbol = input()

print(symbol * m)
for i in range(1, n - 1):
    print(symbol + " " * (m - 2) + symbol)
print(symbol * m)

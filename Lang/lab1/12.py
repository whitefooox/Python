n = int(input())
number = 1
limit = 1
inLine = 0

while number <= n:
    print(number, end=" ")
    number += 1
    inLine += 1
    if inLine == limit:
        print()
        limit += 1
        inLine = 0

n = 8
x = []
y = []
correct = True

for i in range(0, n):
    x_input, y_input = [int(line) for line in input().split()]
    x.append(x_input)
    y.append(y_input)

for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')

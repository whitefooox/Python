number = list(input())

Max = max(number)
Min = min(number)

for i in number:
    if i != Max and i != Min:
        break
if (int(Max) + int(Min)) / 2 == int(i):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")

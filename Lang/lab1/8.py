Max = 150
Min = 190

x = input()
count = 0

while x != "!":
    z = int(x)
    if z > 150 and z < 190:
        count += 1
        if z > Max:
            Max = z
        if z < Min:
            Min = z
    x = input()

print(count)
print(Min, Max)

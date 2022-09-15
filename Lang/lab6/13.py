l = [3, 6, -8, 2, -78, 1, 23, -45, 9]
l.sort(key=abs, reverse=True)
print(*l)
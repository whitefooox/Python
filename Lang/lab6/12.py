l = input().split()
l.sort(key = lambda x: x.lower())
print(*l)
l = list(i for i in range(10, 21))
print(list(map(lambda x: x / 2, filter(lambda x: x > 17, l))))
print(list(x / 2 for x in l if x > 17))
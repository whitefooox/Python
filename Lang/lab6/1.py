l = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x < 5, l)))
print(list(x for x in l if x < 5))

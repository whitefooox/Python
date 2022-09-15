print(sum(map(lambda x: x**2 ,filter(lambda x: x % 9 == 0, 
list(i for i in range(1, 101))))))
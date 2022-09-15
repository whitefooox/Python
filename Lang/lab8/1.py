import numpy as np
#a
arr_1 = np.full((3, 4), 3)
print('a)', arr_1)

#b
arr_2 = np.random.randint(0, 9, size=(2, 4))
print('b)', arr_2)

#c
print('c)', arr_1.size, arr_2.size)

#d
print('d)', np.row_stack((arr_1, arr_2)))

#e
arr_3 = np.array([1, 8, 6, 5, 8, 3])
print('e)', arr_3)

#f
arr_4 = arr_3 * 3 + 1
print('f)', arr_4)

#g
arr_5 = arr_3.reshape((2, 3))
print('g)', arr_5)

#h
print('h)', np.min(arr_5, 1))

#i
print('i)', np.mean(arr_5))

#j
arr_6 = np.square(np.arange(11))
print('j)', arr_6)

#k
print('k)', arr_6[::2])

#l
print('l)', arr_6[::-1])

#m
arr_6[::2] = 2
print('m)', arr_6)

#n
print('n)', 49 in arr_6)

#o
a = np.random.randint(-10, 10, size=(5, 5))
b = a[a < 0]
print('o) (a)', a)
print('o) (b)', b)
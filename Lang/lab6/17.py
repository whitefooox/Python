lst = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
 
res = sum(lst[0])
 
if all([sum(x) == res for x in lst]) and all([sum(x) == res for x in list(zip(*lst))]):
    print('YES')
else:
    print('NO')
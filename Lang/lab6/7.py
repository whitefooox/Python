def alphabet():
    i = ord('А') - 1
    while(i != ord('Я')):
        i += 1
        yield chr(i)

print(list(alphabet()))
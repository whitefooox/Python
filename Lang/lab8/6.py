import random

file = open('res/lines.txt', encoding='utf8')
data = file.read()
lines = data.split('\n')
n = len(lines)
if n:
    line = random.randrange(n)
    print(lines[line])
file.close()
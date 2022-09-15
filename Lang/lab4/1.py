counter = {}

for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(word, counter[word] - 1)

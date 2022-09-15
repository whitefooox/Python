def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1 if objects else True

print(same_by(lambda x: x % 2, [0, 2, 10]))
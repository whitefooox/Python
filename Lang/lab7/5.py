class ReversedList:

    def __init__(self, l):
        self.l = l[::-1]

    def __len__(self):
        return len(self.l)

    def __getitem__(self, index):
        return self.l[index]

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
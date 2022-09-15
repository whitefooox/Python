class Digits:
 
    def __init__(self, l):
        self.l = [int(x) for x in l.split()]
 
    def make_negative(self):
        for i in range(len(self.l)):
            self.l[i] = -abs(self.l[i])
 
    def square(self):
        for i in range(len(self.l)):
            self.l[i] = (self.l[i]) ** 2
 
    def strange_command(self):
        for i in range(len(self.l)):
            if self.l[i] % 5 == 0:
                self.l[i] += 1
 
    def stringify(self):
        for i in range(len(self.l)):
            self.l[i] = str(self.l[i])
            
digits = Digits(input())
for i in range(int(input())):
    operation = input()
    if operation == 'make_negative':
        digits.make_negative()
    elif operation == 'square':
        digits.square()
    else:
        digits.strange_command()
digits.stringify()
print(' '.join(digits.l))
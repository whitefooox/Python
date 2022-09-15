class Summator:

    def transform(self, n):
        return n
 
    def sum(self, N):
        count = 0
        for i in range(N + 1):
            count += self.transform(int(i))
        return count
 
 
class SquareSummator(Summator):
    def __init__(self):
        pass
 
    def transform(self, n):
        return n ** 2
 
 
class CubeSummator(Summator):
    def __init__(self):
        pass
 
    def transform(self, n):
        return n ** 3

N = 10
summator = SquareSummator()
print(summator.sum(N))
print(N * (N + 1) * (2 * N + 1) / 6)
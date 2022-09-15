class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        res = 0
        for i in range(len(self.coefficients)):
            res += pow(x, i) * self.coefficients[i]
        return res

    def __add__(self, other):
        l = []
        res = Polynomial(l)
        if len(self.coefficients) < len(other.coefficients):
            n = len(self.coefficients)
        else:
            n = len(other.coefficients)
        for i in range(n):
            l.append(self.coefficients[i] + other.coefficients[i])
        if len(self.coefficients) > n:
            l += self.coefficients[n::]
        else:
            l += other.coefficients[n::]
        res.coefficients = l
        return res

poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1
 
print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))

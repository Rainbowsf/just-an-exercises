class PearsBasket:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return(str(self.n))

    def __repr__(self):
        return("PearsBasket(" + str(self.n) + ')')

    def __floordiv__(self, x):
        l = []
        k = self.n
        while k > x:
            px = PearsBasket(x)
            l.append(px.__repr__())
            k -= x
        px = PearsBasket(k)
        l.append(px.__repr__())
        return(l)

    def __mod__(self, k):
        return(self.n % k)

    def __add__(self, other):
        return(PearsBasket(self.n + other.n))

    def __sub__(self, y):
        if self.n >= y:
            self.n = self.n - y
        else:
            self.n = 0


pb = PearsBasket(17)
array = pb//4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 %7)
pb - 2
print([pb])
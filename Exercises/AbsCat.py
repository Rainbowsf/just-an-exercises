class AbstractCat:
    def __init__(self):
        self.wgt = 0
        self.kkk = 0

    def eat(self, food):
        self.wgt = self.wgt + (food + self.kkk) // 10
        self.kkk = (food + self.kkk) % 10
        if self.wgt > 100:
            self.wgt = 100

    def __str__(self):
        return('AbstractCat (' + str(self.wgt) + ')')


class Kitten(AbstractCat):
    def __init__(self, wgt):
        self.wgt = wgt

    def meow(self):
        return('meow...')

    def sleep(self):
        self.l = ''
        for i in range(self.wgt // 5):
            self.l += 'Snore'
        return(self.l)


class Cat (Kitten):
    def __init__(self, wgt, name):
        self.wgt = wgt
        self.name = name

    def meow(self):
        return('MEOW...')

    def get_name(self):
        return(str(self.name))

    def catch_mice(self):
        return('Got it!')



abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)
kit = Kitten(25)
print(kit.sleep())
cat = Cat(83, 'Molly')
print(cat.meow())
print(cat.get_name())
print(cat.sleep())
print(cat.catch_mice())
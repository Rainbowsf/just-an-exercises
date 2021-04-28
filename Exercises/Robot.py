class Robot:
    def __init__(self, cor =(0, 0)):
        self.cor = cor
        self.x = self.cor[0]
        self.y = self.cor[1]
        self.l = []
        self.l.append(self.cor)

    def move(self, way):
        self.l = []
        self.l.append(self.cor)
        for el in way:
            if el == 'N':
                self.y += 1
                self.cor = (self.x, self.y)
                self.l.append(self.cor)
            elif el == 'E':
                self.x += 1
                self.cor = (self.x, self.y)
                self.l.append(self.cor)
            elif el == 'W':
                self.x -= 1
                self.cor = (self.x, self.y)
                self.l.append(self.cor)
            elif el == 'S':
                self.y -= 1
                self.cor = (self.x, self.y)
                self.l.append(self.cor)
        return(self.cor)


    def path(self):
        return(self.l)

r = Robot((0, 0))
print(r.move('NENW'))
print(r.move('NENW'))
print(*r.path())
print(r.move('NENW'))
class Horse:
    def __init__(self, num, speed):
        self.num = num
        self.speed = speed
        self.way = self.speed * t

    def laps(self):
        self.lapsq = 0
        while (self.way > M):
            self.way -= M
            self.lapsq += 1
        self.way = M - self.way
        return (float(self.way))


class Auto(Horse):
    def __init__(self, num, speed, benz):
        self.num = num
        self.speed = speed
        self.benz = benz
        if self.benz == 98:
            self.benz = 1
        elif self.benz == 95:
            self.benz = 0.9
        elif self.benz == 92:
            self.benz = 0.8
        self.way = self.speed * self.benz * t


class Moto(Auto):
    def __init__(self, num, speed, benz):
        self.num = num
        self.speed = speed
        self.benz = benz
        if self.benz == 98:
            self.benz = 1
        elif self.benz == 95:
            self.benz = 0.8
        elif self.benz == 92:
            self.benz = 0.6
        self.way = self.speed * self.benz * t


winner = [[1000000, 1000000]]
l1 = input().split()
N=int(l1[0])
M=int(l1[1])
t=int(l1[2])
for j in range(N):
    l1 = input().split()
    num1 = int(l1[0])
    typ = int(l1[1])
    speed1 = int(l1[2])
    if typ == 1:
        benz1 = int(l1[3])
        r = Auto(num1, speed1, benz1)
    elif typ == 2:
        benz1 = int(l1[3])
        r = Moto(num1, speed1, benz1)
    else:
        r = Horse(num1, speed1)
    ddd = r.laps()
    if ddd < float(winner[0][1]):
        winner.clear()
        winner.append([r.num, ddd])
    elif ddd == float(winner[0][1]):
        winner.append([r.num, ddd])
    else:
        pass
win = 100000
for h in range(len(winner)):
    if winner[h][0] < win:
        win = winner[h][0]
print(win)

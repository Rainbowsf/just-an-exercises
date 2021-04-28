def write(l):
    for i in range(n):
        for j in range(7):
            print(l[i][j], end='')
        print('')


def ticket(tickets, pas):
    print('Passengers can take seats:', end='')
    for p in range(pas):
        print('', tickets[p][0], end='')
        print(tickets[p][1], end='')
    print('')
    write(l)


tickets=[]
l = []
n = int(input())
for i in range(n):
    l.append(list(input()))
m = int(input())
for i in range(m):
    b=1
    ask = input().split()
    if ask[0]=='3':
        if ask[1] == 'left':
            for j in range(n):
                if l[j][0] == '.' and l[j][1]=='.' and l[j][2]=='.':
                    l[j][0] = 'X';
                    l[j][1] = 'X';
                    l[j][2] = 'X';

                    tickets.append([j+1, 'A'])
                    tickets.append([j+1, 'B'])
                    tickets.append([j+1, 'C'])
                    ticket(tickets, int(ask[0]))
                    tickets.clear()
                    l[j][0] = '#';
                    l[j][1] = '#';
                    l[j][2] = '#';
                    b=0;
                    break;
        if ask[1] == 'right':
            for j in range(n):
                if l[j][4] == '.' and l[j][5] == '.' and l[j][6] == '.':
                    l[j][4] = 'X';
                    l[j][5] = 'X';
                    l[j][6] = 'X';
                    tickets.append([j+1, 'D'])
                    tickets.append([j+1, 'E'])
                    tickets.append([j+1, 'F'])
                    ticket(tickets, int(ask[0]))
                    tickets.clear()
                    l[j][4] = '#';
                    l[j][5] = '#';
                    l[j][6] = '#';
                    b = 0;
                    break;
    if ask[0]=='2':
        if ask[1] == 'left':
            if ask[2] == 'aisle':
                for j in range(n):
                    if l[j][1] == '.' and l[j][2] == '.':
                        l[j][1] = 'X';
                        l[j][2] = 'X';
                        tickets.append([j + 1, 'B'])
                        tickets.append([j + 1, 'C'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][1] = '#';
                        l[j][2] = '#';
                        b = 0;
                        break;
            if ask[2] == 'window':
                for j in range(n):
                    if l[j][0] == '.' and l[j][1] == '.':
                        l[j][0] = 'X';
                        l[j][1] = 'X';
                        tickets.append([j + 1, 'A'])
                        tickets.append([j + 1, 'B'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][0] = '#';
                        l[j][1] = '#';
                        b = 0;
                        break;
        if ask[1] == 'right':
            if ask[2] == 'aisle':
                for j in range(n):
                    if l[j][4] == '.' and l[j][5] == '.':
                        l[j][4] = 'X';
                        l[j][5] = 'X';
                        tickets.append([j + 1, 'D'])
                        tickets.append([j + 1, 'E'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][4] = '#';
                        l[j][5] = '#';
                        b = 0;
                        break;
            if ask[2] == 'window':
                for j in range(n):
                    if l[j][5] == '.' and l[j][6] == '.':
                        l[j][5] = 'X';
                        l[j][6] = 'X';
                        tickets.append([j + 1, 'E'])
                        tickets.append([j + 1, 'F'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][5] = '#';
                        l[j][6] = '#';
                        b = 0;
                        break;
    if ask[0]=='1':
        if ask[1] == 'left':
            if ask[2] == 'aisle':
                for j in range(n):
                    if l[j][2] == '.':
                        l[j][2] = 'X';
                        tickets.append([j + 1, 'C'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][2] = '#';
                        b = 0;
                        break;
            if ask[2] == 'window':
                for j in range(n):
                    if l[j][0] == '.':
                        l[j][0] = 'X';
                        tickets.append([j + 1, 'A'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][0] = '#';
                        b = 0;
                        break;
        if ask[1] == 'right':
            if ask[2] == 'aisle':
                for j in range(n):
                    if l[j][4] == '.':
                        l[j][4] = 'X';
                        tickets.append([j + 1, 'D'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][4] = '#';
                        b = 0;
                        break;
            if ask[2] == 'window':
                for j in range(n):
                    if l[j][6] == '.':
                        l[j][6] = 'X';
                        tickets.append([j + 1, 'F'])
                        ticket(tickets, int(ask[0]))
                        tickets.clear()
                        l[j][6] = '#';
                        b = 0;
                        break;
    if b == 1:
        print('Cannot fulfill passengers requirements')

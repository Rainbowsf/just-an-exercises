n, k = input().split()
n = int(n)
k = int(k)
s = []
m = []
sum = 0
for j in range(k):
    m.append(1000000000)
l = input().split()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            s.append(abs(int(l[i])-int(l[j])))
    for j in range(n):
        for p in range(k-1):
            if s[j] < m[p]:
                m[p] = s[j]
                for v in range(p, k-1):
                    m[v+1] = m[v]
                break;
    print(m)
    for j in range(k):
        sum += m[j]
    print(sum, end=' ')
    sum = 0
    s.clear()




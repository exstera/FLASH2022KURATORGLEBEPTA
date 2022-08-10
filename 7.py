a = []
s = 0
maxe = 0
n = int(input())
for i in range(0,n):
    e = int(input())
    a.append(e)
    s += a[i]
    maxe = max(maxe,a[i])
if s%2 == 0 or maxe == (s - maxe):
    print('YES')
else:
    print('NO')
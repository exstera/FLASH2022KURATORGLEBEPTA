n = int(input())
a = input().split(' ')
maxk = 0
for i in range(n):
    for j in range(i, n + 1):
        ed = a[i:j].count('1')
        nu = len(a[i:j]) - ed
        diff = nu - ed
        print(ed, nu, diff)
        maxk = max(maxk, diff)
print(maxk)
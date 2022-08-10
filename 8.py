n = int(input())
s = int(input())
a = []
for i in range(n):
    e = int(input())
    a.append(e)
s2 = 0
a.sort()
for i in range(1,len(a)):
    while a[i] != 0:
        if s2 == s:
            break
        a[i] = a[i] - 1
        s2 += 1
        print(a,s2)
if s2 != s:
    while a[0] != 0:
        if s2 == s:
            break
        a[0] = a[0] - 1
        s2 += 1
        print(a,s2)


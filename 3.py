d = 0
c = 0
x = 'ABCDF'
y = 'SDRC'
f = open('1942.txt')
s = f.readline()
for i in range(len(s)-1):
    if s[i] == 'D' and s[i+1] in y:
        d += 1
    if s[i] == 'C' and s[i+1] in y:
        c += 1
print(s.count('A'), s.count('B'), c, d, s.count('F'))
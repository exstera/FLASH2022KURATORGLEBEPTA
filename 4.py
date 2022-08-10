f = open('0976.txt')
s = f.readline()
k = 0
maxk = 0
i = 0
mink = 2321
kc = 0
while i < len(s)-4:
    if ((s[i]=='B') and (s[i+1]=='E') and (s[i+2]=='B') and (s[i+3]=='R') and (s[i+4]=='A')) and (s[i+5] != 'C' and s[i+5] != 'D' and s[i+5] != 'E' and s[i+5] != 'F' and s[i+5] != 'G'):
        k += 1
        maxk = max(maxk,k)
        mink = min(mink,k)
        kc += 1
        i += 5
    else:
        k = 0
        i += 1
print(maxk,mink, kc)
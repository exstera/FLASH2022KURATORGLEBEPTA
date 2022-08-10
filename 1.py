alf = '01234567'
kt = 0
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                for s5 in alf:
                    if (s1 != '0' and s1 != '1' and s1 != '3' and s1 != '5' and s1 != '7') and (s5 != '6' and s5 != '7') and ((s2 == '1' and s4 != '1') or (s2 != '1' and s4 == '1')):
                        s = s1+s2+s3+s4+s5
                        kt += 1

print(s, kt)

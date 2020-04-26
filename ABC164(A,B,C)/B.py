a, b, c, d = map(int, input().split())

f = 0
while (1):
    c -= b
    if c <= 0:
        f = 1
        break
    else:
        pass

    a -= d
    if a <= 0:
        f = 2
        break
    else:
        pass

if f == 1:
    print('Yes')
elif f == 2:
    print('No')
else:
    pass

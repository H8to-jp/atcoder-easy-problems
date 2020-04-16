a, b = map(int, input().split())
S1 = str(a) * b
S2 = str(b) * a

if a < b:
    print(S1)
else:
    print(S2)
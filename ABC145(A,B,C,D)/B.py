n = int(input())
S = input()

cnt = n//2
f = 0
if n%2 == 1:
    f = 1
else:
    for i in range(cnt):
        if S[i] == S[cnt+i]:
            pass
        else:
            f = 1
            break

if f == 0:
    print('Yes')
else:
    print('No')
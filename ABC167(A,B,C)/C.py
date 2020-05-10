n, m, x = map(int, input().split())
CA = [0 for i in range(n)]
for i in range(n):
    CA[i] = list(map(int, input().split()))

ans = 10 ** 7
for i in range(2 ** n):
    TCA = [0 for i in range(m + 1)]
    f = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            TCA = [x + y for (x, y) in zip(TCA, CA[j])]
        else:
            pass
    for j in range(1, m + 1):
        if TCA[j] < x:
            f = 1
            break
        else:
            pass
    if f == 0:
        ans = min(ans, TCA[0])
    else:
        pass
if ans == 10 ** 7:
    print(-1)
else:
    print(ans)
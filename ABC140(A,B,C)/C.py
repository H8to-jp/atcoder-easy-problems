n = int(input())
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i == 0:
        ans += B[0]
    elif i == n - 1:
        ans += B[n - 2]
    else:
        ans += min(B[i - 1], B[i])

print(ans)
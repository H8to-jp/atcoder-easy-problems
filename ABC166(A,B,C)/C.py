n, m = map(int, input().split())
H = list(map(int, input().split()))
A = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if H[a] == H[b]:
        A[a] += 1
        A[b] += 1
    elif H[a] > H[b]:
        A[b] += 1
    else:
        A[a] += 1

ans = 0
for i in range(n):
    if A[i] == 0:
        ans += 1
    else:
        pass
print(ans)
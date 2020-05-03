n, k = map(int, input().split())
A = [0 for i in range(n)]
for i in range(k):
    di = int(input())
    B = list(map(int, input().split()))
    for j in range(di):
        A[B[j] - 1] += 1

ans = 0
for i in range(n):
    if A[i] == 0:
        ans += 1
    else:
        pass
print(ans) 
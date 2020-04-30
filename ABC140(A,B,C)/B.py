n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)

for i in range(1, n):
    if A[i - 1] + 1 == A[i]:
        ans += C[A[i - 1] - 1]
    else:
        pass

print(ans)
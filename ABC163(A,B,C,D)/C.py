n = int(input())
A = list(map(int, input().split()))

R = [0 for i in range(n)]
for i in range(n-1):
    R[A[i]-1] += 1

for i in range(n):
    print(R[i])
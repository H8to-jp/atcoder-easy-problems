n = int(input())
S = [0 for i in range(n)]
for i in range(n):
    S[i] = input()

print(len(set(S)))
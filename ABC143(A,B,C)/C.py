n = int(input())
S = input()

h = 0
ans = 1
for i in range(1, n):
    if S[i] == S[h]:
        pass
    else:
        ans += 1
        h = i
print(ans)
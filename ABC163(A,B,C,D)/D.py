n, k = map(int, input().split())
mod = 10 ** 9 + 7

ans = 0
l = 0   #low
h = 0   #high
for i in range(1, n+2): #O(n)
    l += i - 1
    h += n + 1 - i
    c = (h - l + 1) % mod
    if i >= k:
        ans = (ans + c) % mod
    else:
        pass
print(ans)   
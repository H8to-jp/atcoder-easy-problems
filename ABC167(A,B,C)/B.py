a, b, c, k = map(int, input().split())

ans = 0
if a < k:
    k -= a
    ans += a
    if b < k:
        k -= b 
        ans -= k
    else:
        pass
else:
    ans += k
print(ans)
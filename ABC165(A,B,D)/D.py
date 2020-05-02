a, b, n = map(int, input().split())
t = n // b

if t == 0:
    ans = int(a * n / b) - a * int(n / b)
else:
    ans = 0
    for i in range(t):
        x = b * i + (b - 1)
        if x > n:
            x = n
        else:
            pass
        
        tmp = int(a * x / b) - a * int(x / b)
        
        if tmp > ans:
            ans = tmp
        else:
            break

print(ans)
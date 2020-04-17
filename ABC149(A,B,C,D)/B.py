a, b, k = map(int, input().split())
if a <= k:
    k -= a
    a = 0
    if b <= k:
        k -= b
        b = 0
    else:
        b -= k
        k = 0       
else:
    a -= k
    k = 0
    
print('{0} {1}'.format(a, b))
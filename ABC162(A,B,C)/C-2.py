from sys import setrecursionlimit
setrecursionlimit(1000000)

def Euclid_algorithm(a:int, b:int)->int:
    if a < b:
        a, b = b, a
    else:
        pass
    if b == 0:
        return a
    else:
        return Euclid_algorithm(b, a % b)

k = int(input())
ans = 0
for h in range(1, k+1):
    for i in range(1, k+1):
        for j in range(1, k+1):
            ans += Euclid_algorithm(h, Euclid_algorithm(i, j))
print(ans)

#定数
#1≦n≦2*10^5
n = int(input())
P = list(map(int, input().split())) #O(n)

b = n + 1 #border
ans = 0
for i in range(n):  #O(n)
    if P[i] <= b:
        b = P[i]
        ans += 1
    else:
        pass
print(ans)


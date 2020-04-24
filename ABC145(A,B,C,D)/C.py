from itertools import permutations
n = int(input())
C = [[0, 0] for i in range(n)]    #Coordinate

for i in range(n):
    xi, yi = map(int, input().split())
    C[i][0], C[i][1] = xi, yi

def dis(x1:int, y1:int, x2:int, y2:int):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

ans = 0
R = list(permutations(C))   #Root list
for V in R:
    tmp = 0
    for i in range(len(V)-1):
        tmp += dis(V[i][0], V[i][1], V[i+1][0], V[i+1][1])
    ans += tmp/len(R)

print(ans)
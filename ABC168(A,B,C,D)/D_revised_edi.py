from collections import deque
n, m = map(int, input().split())
TO = [[] for i in range(n)] #隣接リスト adjacency list
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b -1
    TO[a].append(b)
    TO[b].append(a)

#BFS
#変数定義
Q = deque([])
DIST = [-1 for i in range(n)]
PRE = [-1 for i in range(n)]
#初期値の設定
DIST[0] = 0
Q.append(0)
#処理
while len(Q) > 0:
    x = Q.popleft()  
    for i in range(len(TO[x])):
        y = TO[x][i]
        if DIST[y] != -1: continue
        DIST[y] = DIST[x] + 1
        PRE[y] = x
        Q.append(y)

print('Yes')
for i in range(n):
    if i == 0: continue
    ans = PRE[i] + 1 
    print(ans)
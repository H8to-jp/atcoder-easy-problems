from collections import deque
n, m = map(int, input().split())
M = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    M[a].append(b)
    M[b].append(a)
#print(M)

R = [-1 for i in range(n)]
Q = deque([(0, -2)])
while len(Q) > 0:
    t = Q[0][0]
    b = Q[0][1]
    #print(t)
    #print(b)
    Q.popleft()
    if R[t] == -1:
        R[t] = b
        for i in range(len(M[t])):
            if R[M[t][i]] == -1:
                Q.append((M[t][i], t))
            else:
                pass
    else:
        pass
#print(R)

f = 0
for i in range(n):
    if R[i] == -1:
        f = 1
        break  
    else:
        pass

if f == 1:
    print('No')
else:
    print('Yes')
    for i in range(1, n):
        print(R[i] + 1)
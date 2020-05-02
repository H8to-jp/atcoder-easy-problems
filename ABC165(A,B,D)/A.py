k = int(input())
a, b = map(int, input().split())

j = a % k + (b - a)
if a % k ==0 or j >= k:
    print("OK")
else:
    print("NG")
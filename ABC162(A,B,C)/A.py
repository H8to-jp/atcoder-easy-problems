n = int(input())
hundred = n // 100
b = n % 100
ten = b // 10
one = b % 10
    
if hundred == 7 or ten == 7 or one == 7:
    print('Yes')
else:
    print('No')

N = int(input())
o = N % 10
if o == 3:
    print('bon')
elif o == 0 or o == 1 or o == 6 or o == 8 :
    print('pon')
else:
    print('hon')
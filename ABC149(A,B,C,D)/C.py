#定数
#2≦x≦10^5
x = int(input())

f = False   #flag    
x = x - 1
#素数がになるまでインクリメントを続ける
while f == False:
    x += 1
    #素数判定
    def judge_prime_num(a:int)->bool:   #O(√N)
        m = int(a**(1/2)+1)
        for i in range(2, m):
            if a % i == 0:
                return False
            else:
                pass
        return True
    f = judge_prime_num(x)

#答えの出力
print(x)
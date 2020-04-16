#定数
#1≦n≦2*10^5
n = int(input())

#先頭と末尾の数の組み合わせの個数を格納するリストを作成
HT = [[0 for i in range(10)] for j in range(10)] #Head Tail list
for i in range(1, n+1):  #O(n)
    d = len(str(i)) #digit
    hnum = i // (10**(d-1))  #head_num
    tnum = i % 10   #tail_num
    HT[hnum][tnum] += 1

#答えの計算
ans = 0
#headとtailが等しい場合
#9通り
for i in range(1, 10):
    ans += HT[i][i] ** 2
#headとtailが等しくない場合
#36通り
for i in range(1,10):
    for j in range(i+1, 10):
        ans += (HT[i][j] * HT[j][i]) * 2

#答えを出力
print(ans)



    

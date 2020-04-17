#定数入力
#2≦n≦10^5
n, k = map(int, input().split())
r, s, p = map(int, input().split())
T = input()

#計算
ans = 0
for i in range(n):  #O(n)
    #k回前の手は出せないことを考慮
    if i >= k:  #k回から手の制限あり
        #k回前が同じ手かどうか
        if T[i] == T[i-k]:
            #T[i]をfに書き換え
            T = T[:i] + 'f' + T[i+1:]
        else:
            pass
    else:   #0~k-1回までは手の制限なし
        pass
    #i回目のじゃんけんの点数を加算
    if T[i] == 'r': 
        ans += p
    elif T[i] == 's':
        ans += r
    elif T[i] == 'p':
        ans += s
    elif T[i] == 'f':   #手が被るので今回は勝つのをあきらめる
        pass
    else:
        pass    #void

#答えの出力
print(ans)
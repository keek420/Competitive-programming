#section4
#総和の計算

def func(N: int) -> int:
    if N == 1:
        return 1
    else:
        return func(N-1) + N


#GCD
def gcd(M: int, N: int) -> int:
    if M%N == 0:
        return N
    return gcd(N,M%N)

#fib
def fib(N: int )->int:
    if N==1 or N ==2:
        return 1 
    
    return fib(N-1) + fib(N-2)

def fib_1(N: int) -> int:
    dp = [0]*N
    dp[0]= 1
    dp[1]= 1
    for i in range(2,N):
        dp[i] = dp[0] + dp[1]
    return dp[N-1]

def fib_2(N: int) -> int:
    global memo=[0]*N
    memo[0]=memo[1] = 1

    if memo[N] == 0:
        memo[N] = fib_2(N-1) + fib_2(N-2)
    return memo[N]

#部分和問題 on recursive
#Nこの整数aと正の整数Ｗが与えられる。aの中から何個かの整数をえらんだ和でWができるかどうか
def bubunwa(index:int, a:list, W: int) -> bool:
    if W - a[index] == 0:
        return True
    elif index == len(a)-1:
        return False

    return bubunwa(index+1, a, W) or bubunwa(index+1, a, W-a[index])
    

#syo4-1
def tri(N:int)-> int:
    if N==1 or N==2:
        return 1
    elif N==0:
        return 0
    
    return tri(N-1)+tri(N-2)+tri(N-3)

#syo4-2 memo tribocch

class Memo_tri():

    def __init__(self):
        self.memo = {}

    def memo_tri(self,N:int)-> int:
        if N==2:
            self.memo[N] = 1
            return 1
        elif N==0 or N==1:
            self.memo[N] = 0
            return 0
        
        if N in self.memo.keys():
            return self.memo[N]
        
        self.memo[N] =  self.memo_tri(N-1)+self.memo_tri(N-2)+self.memo_tri(N-3)
        return self.memo[N]
        
#syo4-5
#ABC-114 C 
#https://atcoder.jp/contests/abc114/submissions/38660568
N = int(input())
 
ans = 0
 
# 数nについて調べ、末尾に数字を追加した数を再帰的に調べる関数
# use3, use4, use7はそれぞれ3, 5, 7を使ったというフラグ
def dfs(n, use3, use5, use7):
    global ans
    # nを超えていたら打ち切って終了する
    if n > N:    # 再帰のstop !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return
    # 3種類全てを使っていたら答えに加算する
    if use3 and use5 and use7:
        ans += 1
    # 末尾に3, 5, 7をつけた数を再帰的に調べる  数字の末尾に任意の数字を追加する-> 10倍して任意の数字をかける !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    dfs(n*10+3, True, use5, use7)
    dfs(n*10+5, use3, True, use7)
    dfs(n*10+7, use3, use5, True)
 
# 何もしない値（値としては0）から呼び出す
dfs(0, False, False, False)
 
# 答えを出力する
print(ans)

#syo4-7
#memo_bubunwa
class Memo_bu():

    def __init__(self, a:list,N:int):
        self.memo = [False]*(N+1)
        self.a = a
        self.length = len(a)
        self.N = N
    
    def bu(self, index:int, N:int)->bool:
        if self.memo[N]:
            return True
        
        if N == self.a[index]:
            self.memo[N] = True
            return True
        if index == self.length-1:
            return False

        self.memo[N] = self.bu(index+1, N-self.a[index]) or self.bu(index+1, N)

        return self.memo[N]



        
        

        


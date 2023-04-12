
"""
num = int(input())
S = input()
flag = 0

for i in range(1,len(S)):
    if S[i] != S[i-1]:
        continue
    else:
        flag = 1
        break

if flag:
    print("No")
else:
    print("Yes")

p2

S = []
for _ in range(8):
    s = input()
    S.append(s)

alpa = ["a","b","c","d","e","f","g","h"]

for i in range(8):
    for j in range(8):
        if "*" == S[i][j]:
            print(alpa[j]+str(8-i))

      

n, x = map(int,input().split())
A = list(map(int,input().split()))

A = sorted(A)

right = 0
left = 0

while(1):
    if A[right] == A[left] + x:
        print("Yes")
        exit()
    elif A[right] > A[left] + x:
        left += 1
        if left == n:
            break
    elif A[right] < A[left] + x:
        right += 1
        if right == n:
            break
print("No")



import sys
import math
n, m = map(int,input().split())

for x in range(m,n*n+1):
    for a in range(1,int(math.sqrt(x)) + 1):
        if x%a == 0 and x/a<=n:
            print(x)
            sys.exit()
print(-1)

n, d = map(int,input().split())
T = list(map(int,input().split()))
ans = -1
for i in range(len(T)-1):
    if T[i+1] - T[i] <= d:
        ans = T[i+1] 
        break
print(ans)



S = str(input())
con1 = 0
for i in range(len(S)):
    if S[i] == "B":
        con1 += i

con2 = True
a=0
for s in S:
    if s == "K":
        a -= 1
    if s == "R":
        a += 1
    
    if a < 0 or a==2:
        con2 = False



if con1%2 == 1 and con2:
    print("Yes")
else:
    print("No")

S = []

H, W = map(int,input().split())

for _ in range(H):
    s = str(input())
    S.append(s)
ans = []
for a in S:
    s = list(a)
    for i in range(W-1):
        if s[i] == "T" and s[i+1] == "T":
            s[i]   = "P"
            s[i+1] = "C"
    ans.append("".join(s))

for k in ans:
    print(k)

A,B =  map(int,input().split())

ans = 0
while(A != B):
    if A == 0 or B == 0:
        break
    if A>B:
        ans += A//B
        A = A%B
    else:
        ans += B//A
        B = B%A

if ans != 0:
    ans -= 1
print(ans)

from itertools import product
N,K = map(int,input().split())
A = list(map(int,input().split()))

account = []
all_bit =  list(product((0,1), repeat = N))

del all_bit[0]
for bit in all_bit:
    price = 0
    for i in range(N):
        if 1 == bit[i]:
            price+=A[i]
    account.append(price)        

print(sorted(account)[K-1])


N,K = map(int,input().split())
A = list(map(int,input().split()))

dp = [False for _ in range(max(A)*K+1)]
dp[0] = True

for a in A:
    for j in range(max(A)*K+1):
        if j >= a and dp[j-a]:
            dp[j] = True


prices = [i+1 for i in range(max(A)*K+1) if dp[i]]
print(prices[K])



n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 0
cnt = 0
r = 0
for l in range(n):
    while r < n and ans < k:
        ans += a[r]
        r += 1
        cnt += 1
    if ans < k:
        break
    ans -= a[l]
    cnt -= 1

print(cnt)



S = input()
ans = 0
length = len(S)
for i in range(length):

    if S[i] == "U":
        ans += length+i-1 
    elif S[i] == "D":
        ans += 2*length-i-2

print(ans)


N = int(input())
A = list(map(int, input().split()))

num4 = 0
num0 = 0
for a in A:
    if a%4 == 0:
        num4 += 1
    elif a%2 == 0:
        pass
    else:
        num0 += 1

if num0 <= num4 or (num0 + num4 == N and num0-1 == num4):
    print("Yes")
else:
    print("No")



MOD = 998244353 

N = int(input())
A = []
B = []

for _ in  (range(N)):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

def dfs(idx,current):
    if idx == N-2:
        if current == A[idx+1] and current == B[idx+1]:
            return 0
        elif current == A[idx+1] or current == B[idx+1]:
            return 1 
        else:
            return 2
            

    if current == A[idx+1] and current == B[idx+1]:
        return 0
    elif current == A[idx+1]:
        return dfs(idx+1,B[idx+1])
    elif current == B[idx+1]:
        return dfs(idx+1,A[idx+1])
    else:
        return dfs(idx+1,B[idx+1]) + dfs(idx+1,A[idx+1])
    
if N ==1:
    print(2)
else:
    print((dfs(0,A[0])+dfs(0,B[0]))%MOD)



MOD = 998244353 

N = int(input())
data = []
dp = [[0,0] for _ in range(N)]

for _ in  (range(N)):
    a = list(map(int, input().split()))
    data.append(a)

dp[0] = [1,1]
for i in range(1,N):
    for pre in [0,1]:
        for next in [0,1]:
            if data[i-1][pre] != data[i][next]:
                dp[i][next] += dp[i-1][pre]

print(sum(dp[-1])%MOD)

"""

T = int(input())

def get_number_all_reverse(N,S)->int:
    ans = 0
    num1 = 0
    left,right = 0,N-1
    for s in S:
        if s == "1":
            num1+= 1

    while left+1 < right :
        if S[left] == "1":
            while True:
                if S[right]=="1" and left < right:
                    right -= 1
                    ans += 1
                    break
                else:
                    right -= 1
        left += 1
    return ans if ans==num1/2 else -1



for _ in range(T):
    N = int(input())
    S = input()
    print(get_number_all_reverse(N, S))
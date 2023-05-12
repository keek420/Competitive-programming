from sys import stdin
from collections import deque

def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

from math import sqrt

sieve = [1]*(int(sqrt(N))+1)
primes = []
for i in range(2,len(sieve)):
    if sieve[i] == 0:
        continue
    primes.append(i)
    for j in range(i*i,len(sieve),i):
        sieve[j] = 0

prefix_sum = sieve
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i]
ans = 0
# a, b を全探索する
for i in range(len(primes)):
    a = primes[i]
    if a * a * a * a * a >= N:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >= N:
            break
    ans += prefix_sum[isqrt(N // (a * a * b))] - prefix_sum[b]

print(ans)




def search_1(i,j,size):
    global H,W,C
    if i == 0 or j == 0 or i == H-1 or j==W-1 or C[i][j] == ".":
        return size+1
    
    return search_1(i-1,j-1,size+1)


def search_2(i,j,size):
    global H,W,C
    if i == 0 or j == 0 or i == H-1 or j==W-1 or C[i][j] == ".":
        return size+1
    
    search_2(i+1,j-1,size+1)

def search_3(i,j,size):
    global H,W,C
    if i == 0 or j == 0 or i == H-1 or j==W-1 or C[i][j] == ".":
        return size+1
    
    search_3(i-1,j+1,size+1)

def search_4(i,j,size):
    global H,W,C
    if i == 0 or j == 0 or i == H-1 or j==W-1 or C[i][j] == ".":
        return size+1
    search_4(i+1,j+1,size+1)
        


H,W = input_int_multi()

C = [input() for _ in range(H)]
N = [0]*min(H,W)

for i in range(1,W-1):
    for j in range(1,H-1):
        if C[i][j] == C[i-1][j-1] ==  C[i-1][j+1] ==  C[i+1][j-1] ==  C[i+1][j+1] ==  "#":
            s = min( search_1(i-1,j-1,1), search_2(i+1,j-1,1),search_3(i-1,j+1,1),search_4(i+1,j+1,1))
            N[s-1]+=1

print(*N)


N,A,B = input_int_multi()
C = input_int_multi()
i = 1
for c in C:
    if c == A+B:
        print(i)
        exit()
    i+=1

white_list = set()
black_list = set()

INF = 10*9+1


G = [ [0 for _ in range(N)] for _ in range(N)]
min_dis = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u,v = input_int_multi()
    G[u-1][v-1],G[v-1][u-1] = 1,1

K = input_int()
P = []
D = []
for _ in range(K):
    p,d = input_int_multi()
    P.append(p)
    D.append(d)

from collections import deque

for start in range(N):
    visited = [False]*N
    queue = deque([start])
    min_dis[start][start] = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        for next,path in enumerate(G[v]):
            if path == 1 and visited[next] == False:
                visited[next] = True
                min_dis[start][next] = min_dis[start][v] + 1
                queue.append(next)

for i in range(N):
    min_dis[i][i] = INF

for p,d in zip(P,D):
    for ver,dis in enumerate(min_dis[p]):
        if dis < d:
            white_list.add(ver)
            if ver in black_list:
                black_list.remove(ver)
        
        elif dis == d:
            if dis not in white_list:
                black_list.add(ver)

if black_list is not None:
    print("Yes")
    print(black_list)
else:
    print("No")




"""
cnt = 0
left = 0
right = N
idx=0

while 1 < abs(right-left):
    idx = (right+left+1)//2

    print(f"? {idx}")

    i = int(input())

    if i == 0:
        left = idx
    else:
        right = idx
    
    cnt+=1

if cnt <= 18:
    print(f"? {idx+1}")

    k = int(input())

    if i!=k:
        print(f"! {idx}")
        exit()
    else:
        print(f"! {idx-1}")
        exit()

print(f"! {idx}")


"""
N,T = input_int_multi()
C = input_int_multi()
R = input_int_multi()
N = input_int()
S = input_str()
import re

k = re.split("-+",S)


"""
not_T = R[0]
p_T = 0
val_T = 0
no_T = 0
flag1 = False

for i,c,r in enumerate(zip(C,R)):
    if c == T:
        flag1 = True
        if val_T<r:
            p_T = i+1
            val_T = r
    elif c==C[0] and not flag1:
        if not_T < r:
            not_T = r
            no_T = i+1 

if flag1:
    print(p_T)
else:
    print(no_T)










"""
N = input_int()
S = input_str()

flag1 = 0
flag2 = 0
flag3 = 0

for s in S:
    if s=="|":
        flag1 += 1

    if s=="*":
        flag2 += 1

    if flag1 == 1 and flag2 == 1:
        print("in")
        exit()
    
    if flag1 == 0 and flag2 == 1:
        print("out")
        exit()
    if flag1 == 0 and flag2 == 0:
        print("out")
        exit()








import itertools
import operator
a = itertools.accumulate(A)
sums = set(a)

for i in list( itertools.accumulate(A)):
    if i + P in sums and i + P+Q in sums and i + P+Q+R in sums:
        print("Yes")
        exit()
print("No") 
A,B = input_int_multi()

N = int((A/(2*B))**(2/3)-1)
def calc(N):
    global A,B
    return N*B + A/((N+1)**(1/2))
ans = min(calc(N),calc(N+1))
print(ans)



S = input_str_multi()
T = input_str_multi()
len_T = len(T)
pre = [False for _ in range(len(S)+1)]
suf = [False for _ in range(len(S)+1)]

pre[0] = True
for i,s,t in enumerate(zip(S[0:len_T-1],T)):
    if s==t or s=="?" or t=="?":
        pre[i+1] = True
    else:
        break
    
for i,s,t in enumerate(zip(reversed(S[0:len_T-1]),reversed(T))):
    if s==t or s=="?" or t=="?":
        suf[i+1] = True
    else:
        break

suf[0] = True
for i in range(len(T)):
    if pre[i] and suf[len(T)-i]:
        print("Yes")
    else:
        print()

import math
def kamo(strength, exp):
    global A
    return A*strength,exp+1
def atgym(strength, exp):
    global B
    return B+strength, exp+1

X,Y,A,B = input_int_multi()
ans = 0
while A*X<Y and A*X <= X+Y:
    ans += 1
    X *= A

ans += (Y-X)//B

print(ans)


N = input_int()
A = input_int_multi()
S = sum(A)
squre_S = sum([i*i for i in A])
X = round(S/N)
print(squre_S - 2*X*S + N*(X**2))


from bisect import bisect_left,bisect_right

n,q = input_int_multi()
A = input_int_multi()
A.sort()
sums= [0]
ans = 0
for a in A:
    ans += a
    sums.append(ans)    

for _ in range(q):
    x = input_int()
    k = bisect_left(A,x)
    less = k*x-sums[k]
    more = sums[-1] - sums[k] - (n-k)*x  
    print(less + more)

___
a,b,x = input_int_multi()

def is_ok(N):
    global a,b,x
    digits = len(str(N))
    return True if a*N+b*digits < x else False

left = 0
right = 10**9+1

while(abs(right - left) > 1):
    mid = (left+right)//2

    if is_ok(mid):
        left = mid
    else:
        right = mid

print(left)




a,b,c = input_int_multi()

from math import sqrt
if 4*a*b < c**2 -2*c*(a+b) + (a+b)**2:
    print("Yes")
else:
    print("No")


MOD = 998244353
Q = input_int()
S = deque("1")
ans = 1

for _ in range(Q):
    q = input_str_multi()


    if q[0] == "1":
        ans = ans*10+int(q[1])
        S.append(q[1])
    elif q[0] == "2":
        top = S.popleft()
        ans -= int(top)*10**(len((S)))
    else:
        print(ans%MOD)

"""
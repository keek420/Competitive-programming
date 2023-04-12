
def some_input():
    return list(map(int,input().split()))

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
#solutions
#https://kakedashi-engineer.appspot.com/2020/05/08/itp1-7b/
'''
from itertools import combinations
nx = []
while(1):
    n, x = map(int,input().split())
    if n==0 and x==0:
        break
    nx.append((n,x))

for n,x in nx:
    cnt = 0
    for c in list(combinations(range(1,n+1),3)):
        if sum(c)==x:
            cnt += 1
    print (cnt)
'''
#my
'''
n,x = some_input

ways = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if j < x-i-j <= n:
            ways+=1

print(ways)


#https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())

def count_divisors(num):
    ans = 0 
    div= 2
    while num>1:
        while num%div == 0:
            num = num/div
            ans += 1
        div += 1

    return 2**ans
    
odds = [ i for i in range(1,N+1) if i%2==1]
ans = 0
for i in odds:
    if count_divisors(i) == 8:
        ans+=1

print(ans)


#https://atcoder.jp/contests/abc122/tasks/abc122_b

S = input()
ans = 0
suma = 0
for i in S:
    if i in ["A","C","G","T"]:
        suma += 1
    else:
        ans = max(ans,suma)
        suma = 0
    
print(ans)


from itertools import combinations
N,M = some_input()
A = [[]*M for _ in range(N)]
lis = combinations(range(M),2)
for i in range(N):
    k = some_input()
    A[i] = k
ans = 0
for l,r in lis:
    su = 0
    for i in range(N):
        su += max(A[i][l],A[i][r])
    ans = max(ans,su)

print(ans)


A,B,C,X,Y = some_input()
ans = 0
if A+B >= 2*C:
    min_c = min(X,Y)
    ans += 2*C*min_c
    if X>=Y:
        ans += A*(X-Y)
    else:
        ans += B*(Y-X)
    
else:
    ans +=A*X+B*Y

print(ans)


from itertools import combinations

N = int(input())
S = input()
ans = 0
lis = combinations(range(N-3),3)
ans_list = []
for idx in len(lis):
    i,j,k = lis[idx]
    string = S[i]+S[j]+S[k]
    if not string in ans_list:
        ans_list.append(string)
        ans += 1

print(ans)

https://kakedashi-engineer.appspot.com/2020/05/16/sumitrust2019d/

N = int(input())
S = input()

st = [set() for _ in range(3)]

for s in S:
    for pre in st[1]:
        st[2].add(pre+s) # 3桁目
    for pre in st[0]:
        st[1].add(pre+s) # 2桁目
    st[0].add(s) # 1桁目
        
print (len(st[2]))



A = []
B = []

N = int(input())

for i in range(N):
    a,b = some_input()
    A.append(a)
    B.append(b)

sum_AB = sum(B)-sum(A)
ans = 10**10
for start in range(100):
    for end in range(start,100):
        sums = 0
        for a,b in zip(A,B):
            sums += abs(a-start)+abs(end-b)
        ans = min(ans,sums)

print(ans+sum_AB)


https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=jaG



n = int(input())

A = some_input()

q = int(input())

Q = some_input()
A.sort()
Q.sort()
from itertools import product
ans ={}
for i in product([0,1],repeat=n):
    sm = 0
    for j in range(n):
        if i[j] == 1:
            sm += A[j]
    ans[sm] = 1

for m in Q:
    if ans[m]:
        print("Yes")
    
def some_input():
    return list(map(int,input().split()))

from itertools import product
from tabnanny import check

N,M = some_input()
K = []
S = []

for _ in range(M):
    inp = some_input()
    K.append(inp[0])
    S.append(inp[1:])
P = some_input()

swhichs =  product([0,1],repeat=N)
ways =0
for case_swichs in swhichs:
    check = 0
    for i in range(M):
        su = 0
        
        for j in range(len(S[i])):
            if case_swichs[S[i][j]-1] == 1:
                su +=1
        if su%2 == P[i]:
            check += 1
            continue
        else:
            break
    if check == M:
        ways += 1

print(ways)
    

from itertools import combinations

N,M = some_input()
G =[[] for _ in range(N)]

for _ in range(M):
    x,y = some_input()
    G[x-1].append(y-1)


flag = 0
for i in range(N,1,-1):
    for j in combinations(range(N),i):
        for k in combinations(j,2):
            if not k[1] in G[k[0]]:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            print(i)
        

                
from itertools import product
R, C = map(int,input().split())
lines = []
for r in range(R):
    line = list(map(int,input().split()))
    lines.append(line)
lines = list(zip(*lines))
ans = 0
for p in product((0,1),repeat=R):
    sm = 0
    for line in lines:
        cnt = 0
        for r in range(R):
            if p[r] == line[r]:
                cnt += 1
        sm += max(cnt, R-cnt)
    ans = max(ans, sm)
print (ans)

'''

N,K = some_input()
A=some_input()
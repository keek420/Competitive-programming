from sys import stdin
def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

N,M,K = input_int_multi()
G = [[] for i in range(K+1) ]
for i in range(M):
    a,b = input_int_multi()
    G[a].append(b)
    G[b].append(a)
ans = set()

from sys import stdin
def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

N,M,K = input_int_multi()
G = [ [] for i in range(N+1) ]
for i in range(M):
    a,b = input_int_multi()
    G[a].append([b])
    G[b].append([a])

query = []
seen = [-1 for i in range(N+1)]



for i in range(K):
    p,h = input_int_multi()
    query.append((-h,p))

import heapq

hquery = heapq.heapfy(query)

while hquery:
  h,p = hquery.heappop()
  h = -h
  
  for v in G[p]:
    if seen[v] != -1 and seen[v] >= h:
      continue
    if h == 0:
      continue
    seen[v] = h
    hquery.heappush((-(h-1),v))
    
ans = []
                    
for i in range(1,N+1):
	if seen[i] != 1:
		ans.append(i)

from sys import stdin
def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

N,M,K = input_int_multi()
G = [ [] for i in range(N+1) ]
for i in range(M):
    a,b = input_int_multi()
    G[a].append(b)
    G[b].append(a)

hquery = []
seen = [-1 for i in range(N+1)]



for i in range(K):
    p,h = input_int_multi()
    hquery.append((-h,p))

import heapq


while hquery:

    h,p = heapq.heappop(hquery)
    h = -h

    for v in G[p]:
        if seen[v] != -1 and seen[v] >= h:
            continue
        if h == 0:
            continue
        if seen[v] == -1:
            seen[v] = h
            heapq.heappush(hquery, (-(h-1),v))
            
        if seen[v] < h:
            seen[v] = h
            heapq.heappush(hquery, (-(h-1),v))
ans = []
print(seen)           
for i in range(1,N+1):
	if seen[i] != 1:
		ans.append(i)
print(len(ans))
print(*ans)




print(len(ans))
print(*sorted(ans))




def dfs(v,hp):
    if hp == 0:
        return
    
    for j in G[v]:
        if hp == 1 and j in ans:
            continue
        
        ans.add(j)
        dfs(j,hp-1)

for i in range(K):
    p,h = input_int_multi()
    dfs(p,h)

print(sorted(ans))





import bisect
N  = input_int()
A = input_int_multi()
Q = input_int()

sums = []
idx_dic = {}
sub_sum = 0
guuki = 0
for i in range(len(A)):
    idx_dic[i] = A[i]

    if guuki % 2 ==0:
        sums.append(sub_sum)
    else:
        sub_sum += A[i] - A[i-1]
        sums.append()
    guuki += 1
        
    

for i in range(Q):
    l,r = input_int_multi()

    left = bisect.bisect_left(A, l)
    right = bisect.bisect_left(A, r)
    ans = 0
    if left % 2 == 1:
        ans += l - A[left]
    if right % 2 == 1:
        ans += r - A[right]
    ans += sum[right] - sums[left] 
    print(ans)





H,W = input_int_multi()

S = []

for i in range(H):
    for j in range(W):
        s = input_str_multi()
        S.append(s)

com = []

for i in range(H):
    s = S[i]
    if all([ ele == "." for ele in s]):
        continue
    com.append




















dis = [0,3,1,4,1,5,5]
dis_sum_dic = {}
acc = 0
for al, d in zip("ABCDEFD", range(len(dis))):
    acc += d
    dis_sum_dic[al] = acc 


p,q = input_int_multi()


print(abs(dis_sum_dic[p]-dis_sum_dic[q]))













mizu = [i for i in range(0,101,5)]

N = input_int()

for j in mizu:
    if abs(j-N) < 3:
        print(j)
        exit()
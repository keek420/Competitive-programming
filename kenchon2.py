def binary_search(a: list, N: int) -> int:
    right, left = len(a) - 1, 0

    while right >= left:
        mid = (left + right) // 2
        if a[mid] == N:
            return mid
        elif a[mid] < N:
            left = mid + 1
        else:
            right = mid - 1
        
    return left
    

#at abc 023 D

def syageki(N:int, H:list, S:list)->int:
    left, right = 0, 10**10
    t = [0 for i in range(N)]
    ok = True

    while left <= right:
        mid = (left + right)//2
        for i in range(N):
            if (mid < H[i]):
                ok = False
            else:
                t[i] = (mid - H[i])//S[i]
        
        t.sort()
        for i in range(N):
            if t[i] < i:
                ok = False
        
        if ok:
            left = mid + 1
        else:
            right = mid -1

    return right
        

#syo6-1
# compress coodrinate

def 6_1(N:int, a:list)->list:
    sorted_a = sorted(a)
    rank = [0 for i in range(N)]

    for idx,val in enumerate(a):
        rank[idx] = binary_search(b, val)
    
    return rank

#syo6-2
#ABC 07 C
from bisect import bisect_left, bisect_right

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

res = 0

for j in range(N):
    Aj = bisect_left(a, b[j])
    Cj = N - bisect_right(c, b[j])
    res += Aj * Cj

def fes(N: int, a:list, b:list, c:list)->int:
    a.sort()
    b.sort()
    c.sort()
    ans = 0

    for idx,val in enumerate(b):
        a_lt_val =  binary_search(a, val) + 1
        c_mt_val =  N - binary_search(c, val) - 1
        ans += a_lt_val*c_mt_val 
    return ans


#syo6-3
#jOI 7 3 darts

def sum_4(N:int, a:list, M:int)->int:
    S = []
    
    for i in a:
        for j in a:
            S.append(i+j)

    S.sort()

    ans = 0

    for i in S:
        idx = binary_search(S, M-i)
        ans = max(ans,i+S[idx])

#syo6-4
#POJ 2456
def agg(N:int, a:int, M:int)->int:
    left,right = 0,a[-1]
    ok = True

    while left<=right:
        mid = (left-right)//2
        cnt = 1
        prev = 0
        for idx,val in enumerate(a):
            if val - a[prev] >= mid:
                prev = idx
                cnt += 1
        
        if cnt < M:
            ok = False

        if ok:
            left = mid + 1
        else:
            right = mid - 1
        
    return left


#syo6-5
#ARC 037 C

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sort b in ascending order
b.sort()

# Check function for binary search
def check(x):
    cnt = 0
    for i in range(N):
        cnt += len(b) - bisect.bisect_right(b, x // a[i])
    return cnt >= K

# Binary search
left, right = 0, 10**18
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid


from bisect import bisect_left, bisect_right

class Okumas()
    def __init__(N:int, a:list, b:list, K:int):
        self.N = N
        self.a,self.b=sorted(a),sorted(b)
        self.K = K

    def check(self, mid:int):
        cnt = 0
        for i in range(self.N):
            cnt += self.N - bisect_right(self.b, mid//self.a[i])
        
        return cnt >= self.K


    def okumasu(self):
        C = self.a[-1]*self.b[-1]

        left, right = 0,C

        while left <= right:
            mid = (left + right )//2

            if check(mid):
                left = mid + 1
            else:
                right = mid - -1

        return right 


#syo6-7
#ARC 101 D


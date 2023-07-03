from sys import stdin
def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

import sys
sys.setrecursionlimit(10**5)

def input_str():
    return sys.stdin.readline().rstrip()

def input_int():
    return int(sys.stdin.readline().rstrip())

def input_str_multi():
    return sys.stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int, sys.stdin.readline().split()))

from sys import stdin
def input_str():
    return stdin.readline().rstrip()

def input_int():
    return int(stdin.readline().rstrip())

def input_str_multi():
    return stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int,input().split()))

import sys
sys.setrecursionlimit(10**5)

def input_str():
    return sys.stdin.readline().rstrip()

def input_int():
    return int(sys.stdin.readline().rstrip())

def input_str_multi():
    return sys.stdin.readline().rstrip().split()

def input_int_multi():
    return list(map(int, sys.stdin.readline().split()))

H, W = input_int_multi()

maze = []
ok = [[True for _ in range(W)] for _ in range(H)]
for _ in range(H):
    maze.append(input_str())

def dfs(x, y, stat,  ok):
    snuke = "snuke"
    next_dir = snuke[stat]
    #print(x,y,next_dir)
    print(x,y,maze[y][x])
    if x == W-1 and y == H-1:
        return True

    if x > 0:
        if maze[y][x-1] == next_dir and ok[y][x-1]:
            ok[y][x-1] = False
            if dfs(x-1, y, (stat+1) % 5, ok):
                return True
    
    if y > 0 :
        if maze[y-1][x] == next_dir and ok[y-1][x]:
            ok[y-1][x] = False
            if dfs(x, y-1, (stat+1) % 5, ok):
                return True
    
    if x < H-1:
        if maze[y][x+1] == next_dir and ok[y][x+1]:
            ok[y][x+1] = False
            if dfs(x+1, y, (stat+1) % 5, ok):
                return True
    
    if y < W-1  :
        if maze[y+1][x] == next_dir and ok[y+1][x]:
            ok[y+1][x] = False
            if dfs(x, y+1, (stat+1) % 5, ok):
                return True
    ok[y][x] = False
    print(ok)
    return False

print("Yes" if dfs(0, 0, 1) else "No")





H, W = input_int_multi()

maze = []
ok = [[True for _ in range(W)] for _ in range(H)]
for _ in range(H):
    maze.append(input_str())

def dfs(x, y, stat):
    snuke = "snuke"
    next_dir = snuke[stat]
    print(x,y,next_dir)
    if x == W-1 and y == H-1:
        return True
    
    if y > 0:
        if maze[y][x-1] == next_dir and ok[y][x-1]:
            if dfs(x-1, y, (stat+1) % 5):
                return True
    
    if x > 0 :
        if maze[y-1][x] == next_dir and ok[y-1][x]:
            if dfs(x, y-1, (stat+1) % 5):
                return True
    
    if x < H-1:
        if maze[y][x+1] == next_dir and ok[x][y+1]:
            if dfs(x+1, y, (stat+1) % 5):
                return True
    
    if y < W-1  :
        if maze[y+1][x] == next_dir and ok[y+1][x]:
            if dfs(x, y+1, (stat+1) % 5):
                return True
    #ok[y][x] = False
    return False

print("Yes" if dfs(0, 0, 1) else "No")















H,W = input_int_multi()

maze = []

for _ in range(H):
    maze.append(input_str())

def dfs( x, y, stat):
    
    snuk = "snuk"
    next = snuk[(stat+1)%4]
    if (x == H and y == W ):
        return True

    if(y>0 and maze[x][y-1] == next):
        if dfs(x,y-1,stat+1):
            return True
    if(x>0 and maze[x-1][y] == next):
        if dfs(x-1,y,stat+1):
            return True
    if(y<W-1 and maze[x][y+1] == next):
        if dfs(x,y+1,stat+1):
            return True
    if(x<H-1 and maze[x+1][y] == next):
        if dfs(x+1,y,stat+1):
            return True

print("Yes" if dfs(0,0,0) else "No")






N = input_int()
A,B = [],[]

for _ in range(N):
    a,b = input_int_multi()
    A.append(a)
    B.append(b)
people = []
for i in range(N):
    people.append( (i+1, A[i]/(A[i]+B[i])))

people.sort(key = lambda x: -x[1])

print(people[0] for people in people)


N,M =input_int_multi()
C = input_int_multi()
D = input_int_multi()
P = input_int_multi()

def calculate_total_cost(N, C, M, D, P, P0):
    total = 0

    for i in range(N):
        color = C[i]
        if color in D:
            index = D.index(color)
            total += P[index]
        else:
            total += P0
    
    return total

print(calculate_total_cost(N, C, M, D, P[1:], P[0]):)

S = input_int_multi()
p_s = S[0]
if(p_s % 25 != 0 or not (100 <= p_s <= 675)):
    print("No")
    exit(1)
for i in range(1,len(S)):
    next_s = S[i]
    if(next_s % 25 != 0 or not (100 <= next_s <= 675)):
        print("No")
        exit(1)
    if(p_s > next_s):
        print("No")
        exit(1)
    p_s = next_s

print("Yes")
    
#linear search method 
#N個の整数a1,a2...aNと整数値vが与えられる、ai=vとなるデータの判定

def linear_search_method(a -> list, v -> float):
    return 1 if v in a else -1

#indexも
def linear_search_method_index(a -> list, v -> float):
    return a.index(v) if v in a else -1

#minimum
def linear_min(a -> list, v -> float):
    min_val = a[0]
    for val in a:
        if a[0] < min_val:
            min_val = a[0]
    return min_val

#Nこの整数aとｂが与えらえる。二つの列から１つずつとって和がＫ以上となる最小値をもとめよ
def linear_pear(a -> list, b -> list, K -> int):
    tmp_min = 10**100
    for a_val in a:
        for b_val in b:
            if a_val + b_val >= K:
                tmp_min = min(tmp_min, a_val + b_val)
    return tmp_min

#Nこの整数aと正の整数Ｗが与えられる。aの中から何個かの整数をえらんだ和でWができるかどうか
def linear_bit (a -> list, N -> int,W -> int):
    for bit in range(2**N):
        sum_1 = 0
        for i in range(N):
            if bit & (1 << i):
                sum_1 += a[i]
        if sum_1 == W:
            return 1

#章末
#3-2
def syo_3_2(a -> list, v -> float):
    cnt = 0
    for a_val in a:
        if a_val == v:
            cnt+= 1
    return cnt



#3-3
def syo_3_3(a -> list, v -> float):
    min_1, min_2 = min(a[0],a[1]), max(a[0],a[1])
    for a_val in a:
        if min_1 < a_val < min_2:
            min_2 = a_val
        elif a_val < min_1:
            min_1,min_2 = a_val,min_1
    return min_2

#syo3-4
def syo3_4(a -> list):
    min_val,max_val = a[0],max_val

    for a_val in a:
        if a_val < min_val:
            min_val = a_val
        elif max_val < a_val:
            max_val = a_val

    return max_val-min_val

#syo3-5
def syo_3_5(a -> list):
    cnt = 0
    while:
        for i in range(len(a)):
            a[i]/=2 if a[i]%2 == 0 and a[i]!= 0 else return cnt
        cnt += 1

#syo3-6
def syo3_6(K -> int, N -> int):
    cnt = 0
    for X in range(K):
        for Y in range(K):
            if 0 <= N-X-Y and N-X-Y <= K:
                cnt += 1
    return cnt

def syo3_7( S: str):
    n = len(S)
    pre = 0
    ans = 0
    for bit in range(2**n):
        tmp = 0
        for j in range(n):
            if i & 1<<j:
                tmp += int(S[pre:j])
                pre = j+1
        ans += tmp
    return ans


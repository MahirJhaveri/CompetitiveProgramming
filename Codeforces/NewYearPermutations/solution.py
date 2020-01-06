# 1279E - New Year Permutations

# Idea:
# dp(i) --> # of good permutations of [i,n]
# cycles(m) --> # of blocks of len m ( == (m-2)! as first element is fixed)
# It is easy to test for impossibility ie.  k > dp(1)
# Another subproblem: how to compute jth smallest cycle
# getGoodPerm(n,k) uses both getCycle(b, (k/dp[n-b])) and getGoodPerm(n-b, k%dp[n-b])


# TIME LIMIT EXCEEDED

import math
from decimal import *

getcontext().prec = 50


# simple implementation of the union find
class DSU:
    def __init__(self, n):
        self.hash = {}
        for i in range(1, n+1):
            self.hash[i] = [i]

    def union(self, i, j):
        lst1 = self.hash[i]
        lst2 = self.hash[j]
        lst1.extend(lst2)
        for element in lst2:
            self.hash[element] = lst1

    def same_set(self, i, j):
        return j in self.hash[i]


def getKthCycle(n, k, fact):
    lst = [i-1 for i in range(n+1)]
    # num of ends that still dont have incoming link
    num_open = n

    dsu = DSU(n)
    dsu.union(1, n)
    lst[1] = n
    num_open -= 1

    pos = 2
    while pos < n:
        i = pos
        while i <= n:
            if dsu.same_set(pos, lst[i]):
                pass
            else:
                if k <= fact[num_open-2]:
                    break
                else:
                    k -= fact[num_open-2]
            i += 1

        if i == n+1:  # k is too large
            return None
        else:
            num_open -= 1

            dsu.union(pos, lst[i])

            # move the element at pos i to "pos"
            # while keeping the sorted-ness of lst
            temp = lst[i]
            j = i
            while j > pos:
                lst[j] = lst[j-1]
                j -= 1
            lst[pos] = temp

        pos += 1
    return lst[1:]


# number of cycles with n elements
def cycles(n, fact):
    if n <= 1:
        return 1
    else:
        if n-2 in fact:
            return fact[n-2]
        else:
            return math.factorial(n-2)


def Max(i, table, fact):
    if i in table:
        return table[i]
    else:
        if i <= 1:
            table[i] = 1
            return 1
        else:
            val = 0
            for j in range(1, i+1):
                val += Max(i-j, table, fact)*cycles(j, fact)
            table[i] = val
            return val


def getKthGoodPermutation(n, k, Max, fact):
    if Max[n] < k:  # k is too large
        return None
    if n == 1:
        if k == 1:
            return [1]
        else:
            return None

    block_len = 1
    while k - cycles(block_len, fact)*Max[n-block_len] > 0:
        k -= cycles(block_len, fact)*Max[n-block_len]
        block_len += 1

    k_block = math.ceil(Decimal(k)/Decimal(Max[n-block_len]))
    k_rem = k - (k_block - 1)*Max[n-block_len]

    new_lst = getKthCycle(block_len, k_block, fact)
    if n-block_len > 0:
        rem_lst = getKthGoodPermutation(n-block_len, k_rem, Max, fact)
        for i in range(len(rem_lst)):
            rem_lst[i] += block_len
        new_lst.extend(rem_lst)
    return new_lst


def compute_fact(n, table):
    table[0] = 1
    table[1] = 1
    x = 2
    while x <= n:
        table[x] = x*table[x-1]
        x += 1
    return


if __name__ == '__main__':
    T = int(input())
    N, K = [], []
    for _ in range(T):
        inp = input().rstrip().split(" ")
        n, k = int(inp[0]), int(inp[1])
        N.append(n)
        K.append(k)

    # prepare tables
    max_n = max(N) + 5
    fact = {}
    compute_fact(max_n, fact)

    dp_table = {}
    a = 1
    while a <= max_n:
        Max(a, dp_table, fact)
        a += 1

    j = 0
    while j < len(N):
        lst = getKthGoodPermutation(N[j], K[j], dp_table, fact)
        if lst != None:
            for i in range(len(lst)):
                lst[i] = str(lst[i])
            print(" ".join(lst))
        else:
            print("-1")
        j += 1

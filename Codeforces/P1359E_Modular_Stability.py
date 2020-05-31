# Problem 1359E - Modular Stability

import time
import math

inp = input().rstrip().split()
n, k = int(inp[0]), int(inp[1])

MOD = 998244353

def C(n,k):
    if k > n:
        return 0
    elif n == 0 and k ==0:
        return 1
    else:
        return fact[n]*inv(fact[k]*fact[n-k], MOD) % MOD

ans = 0

# response == (gcd, x, y)
def extendedGCD(a, b):
    if (a == 0):
        return (b,0,1)
    else:
        (d1, x1, y1) = extendedGCD(b%a, a)
        new_x = y1 - (b//a)*x1
        new_y = x1
        return (d1, new_x, new_y) 

def inv(b, m):
    (d, x, y) = extendedGCD(b, m)
    return (x%m + m) % m

# precompute the factorials mod 998244353
fact = {}
fact[0] = 1
i=1
prod = 1
while i <= n:
    prod = prod*i % MOD
    fact[i] = prod
    i += 1

m = 1
upper_limit = math.floor(n*1.0/k)
while m <= upper_limit:
    ans += C(math.floor(n/m)-1, k-1)
    ans = ans % MOD 
    m += 1
print(ans)

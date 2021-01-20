# Problem 1474B - Different Divisors

def isPrime(n) : 
 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

def main():
    T = int(input())
    for c in range(T):
        d = int(input())
        p = d+1
        while not isPrime(p):
            p += 1
        q = p + d
        while (not isPrime(q)) and q < p*p:
            q+=1
        print(p*q)

main()

# Problem 1012 - Numbers with Repeated Digits

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        
        arr = get_arr(N+1)
        
        fact = {0:1}
        i = 1
        while i <= 9:
            fact[i] = fact[i-1]*i
            i += 1
        
        ans = 0
        l = 1
        while l < len(arr):
            ans += (fact[9]*9)/(fact[9-l]*(10-l))
            l += 1
        
        used = [0 for i in range(10)]
        i = 0
        while i < len(arr):
            # case 1: 
            avail = getFreePos(used, arr[i]) - 1 if i == 0 else getFreePos(used, arr[i])
            rem = 10 - (totalUsed(used) + 1)
            ans += (avail)*(fact[rem]/fact[rem - (len(arr)-i-1)])
            #print(ans)
            
            if used[arr[i]] == 1:
                break
            
            # case 2:
            used[arr[i]] = 1
            
            i += 1
        
        return N - ans
        
        

def get_arr(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n / 10
    arr.reverse()
    return arr

def getFreePos(bitmap, pos):
    ans = 0
    i = 0
    while i < pos:
        if bitmap[i] == 0:
            ans += 1
        i += 1
    return ans

def totalUsed(bitmap):
    return 10 - getFreePos(bitmap, len(bitmap))

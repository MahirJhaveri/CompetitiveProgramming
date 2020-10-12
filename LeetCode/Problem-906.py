# 906. Super Palindromes

class Solution(object):
    
    # strategy check between sql_l and sq_r
    # 10^9 is the length of the range - still not trivial
    # only look at palindromes in that range - 10^5 nums - since the other half of the number is fixed
    # Finally check if the square is also a palindrome
    
    def superpalindromesInRange(self, L, R):
        L = int(L)
        R = int(R)
        
        count = 0
        
        UPPERLIMIT = 100000
        
        # check all nos between 0 and UPPERLIMIT
        
        for x in range(UPPERLIMIT):
            s = str(x)
            p1 = int(s + s[::-1])
            p2 = int(s if len(s) == 0 else s + s[-2::-1])
            
            n1 = p1 ** 2
            n2 = p2 ** 2
            
            if L <= n1 and n1 <= R:
                if is_palindrome(n1):
                    print(n1)
                    count += 1
            
            if L <= n2 and n2 <= R:
                if is_palindrome(n2):
                    print(n2)
                    count += 1
        
        return count
    
# checks if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]
        

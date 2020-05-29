# Palindromic Substrings

class Solution(object):
    
    def countSubstrings(self, s):
        if len(s) == 0:
            return 0
        
        # init the table first
        n = len(s)
        for i in range(n*n):
            table[i] = None
        
        for start in range(n):
            table[start*n+start] = True
        
        count = 0
        
        for start in range(n):
            for end in range(start, n):
                if dp_get(start, end, n,s) == True:
                    count += 1
        return count
                    

table = {}


def dp_get(start, end, n, s):
    if end <= start:
        return True
    
    if table[start*n+end] == None:
        if s[start] == s[end]:
            table[start*n+end] = dp_get(start+1, end-1, n, s)
        else:
            table[start*n+end] = False
    return table[start*n+end]

# Problem 1849 - Splitting a String Into Descending Consecutive Values

def splitStringAux(s, start=None):
    if len(s) == 0 or int(s) == start:
        return True
    for i in range(1,len(s)):
        if start == None or int(s[:i]) == start:
            if start != None and i == len(s):
                return True
            if splitStringAux(s[i:], int(s[:i])-1) == True:
                return True
    return False

class Solution:
    def splitString(self, s: str) -> bool:
        return splitStringAux(s, None)
        

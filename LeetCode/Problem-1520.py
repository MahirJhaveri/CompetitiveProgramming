# Problem 1520 - Maximum Number of Non-Overlapping Substrings

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        r = {}
        for i in range(len(s)):
            c=s[i]
            if c not in r:
                r[c] = [i,i]
            else:
                r[c][1] = i
        
        # first compute the ranges for min-subtrings starting at each possible letter
        chars = []
        for c in s:
            if c not in chars:
                chars.append(c)
        
        l = []
        for st in chars:
            rng = [r[st][0], r[st][1]]
            i = r[st][0]
            psbl = True
            while i <= rng[1]:
                c = s[i]
                if r[c][0] < rng[0]:
                    psbl = False
                    break
                else:
                    rng[1] = max(rng[1], r[c][1])
                i += 1
            if psbl:
                l.append(rng)
        
        l.sort(key=lambda tup: (tup[1], -1*tup[0]), reverse=True)
        
        ans = []
        
        i=0
        while len(l) > 0:
            ss = l.pop()
            if ss[0] >= i:
                ans.append(s[ss[0]:ss[1]+1])
                i = ss[1]+1
        return ans

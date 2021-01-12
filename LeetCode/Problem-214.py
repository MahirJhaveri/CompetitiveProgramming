# Problem 214 - Shortest Palindrome

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = s + "#" + s[::-1]
        f = [0 for i in range(2*len(s)+1)]
        i = 1
        while i < 2*len(s)+1:
            t = f[i-1]
            while t > 0 and new_s[i] != new_s[t]:
                t = f[t-1]
            if new_s[i] == new_s[t]:
                f[i] = t+1
            i += 1
        return s[f[2*len(s)]:][::-1] + s

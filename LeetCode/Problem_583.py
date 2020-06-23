# Problem 583: Delete Operation for Two Strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = {}
       
        # init table (base case)
        for i in range(0, len(word1)+1):
            table[i] = {0:i}
        for j in range(0,len(word2)+1):
            table[0][j] = j
       
        for i in range(1,len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(table[i-1][j], table[i][j-1]) + 1
       
        return table[len(word1)][len(word2)]

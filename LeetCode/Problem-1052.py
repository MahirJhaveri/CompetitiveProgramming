# Problem 1052: Grumpy Bookstore Owner

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        min_score = 0
        ans = 0
        temp = 0
        i=0
        while i <= X-1:
            min_score += customers[i]*(grumpy[i]-1)*-1
            temp += customers[i]*grumpy[i]
            i+=1
        while i<len(grumpy):
            min_score += customers[i]*(grumpy[i]-1)*-1
            ans = ans if temp <= ans else temp
            temp -= customers[i-X]*grumpy[i-X]
            temp += customers[i]*grumpy[i]
            i += 1
        ans = ans if temp <= ans else temp
        return ans + min_score

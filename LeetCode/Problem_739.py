# Problem 739: Daily Temperatures

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = []
        i = len(T)-1
        while i >= 0:
            while len(stack) > 0:
                (top, index) = stack.pop()
                if top > T[i]:
                    stack.append((top, index))
                    break
            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(index - i)
            stack.append((T[i], i))
            i -= 1
        ans.reverse()
        return ans

# Problem 1567 - Maximum Length of Subarray With Positive Product

class Solution(object):
    def getMaxLen(self, nums):
        ans = 0
        largestPos = None
        largestNeg = None
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                largestPos = None
                largestNeg = None
            elif nums[i] > 0:
                if largestPos:
                    largestPos += 1
                else:
                    largestPos = 1
                if largestNeg:
                    largestNeg += 1
                ans = largestPos if largestPos > ans else ans
            else:
                temp = largestNeg
                if largestPos:
                    largestNeg = largestPos + 1
                else:
                    largestNeg = 1
                if temp:
                    largestPos = temp + 1
                    ans = largestPos if largestPos > ans else ans
                else:
                    largestPos = None
            i += 1
        return ans
        

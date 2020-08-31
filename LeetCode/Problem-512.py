class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        min_neg = None
        prod = 1
        ans = -100000000000
        
        while i < len(nums):
            if nums[i] == 0:
                ans = max(ans, 0)
                min_neg = None
                prod = 1
            else:
                prod = prod * nums[i]
                if prod > 0:
                    ans = max(ans, prod)
                elif not min_neg:
                    ans = max(ans, prod)
                    min_neg = prod
                else:
                    ans = max(prod/min_neg, ans)
                    min_neg = max(min_neg, prod)
                
            i += 1
        return ans

# Problem 209: Minimum size subarray sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = 1000000000
        ans=1000000000
        n = len(nums)
        nums.append(0)
        sum1 = nums[0]
        sum2 = 0
        start = end = 0
        while end < n:
            while sum1 - sum2 - nums[start] >= s and start <= end:
                sum2 += nums[start]
                start += 1
            if sum1 - sum2 >= s:
                #print(start, end)
                ans = min(ans, end-start+1)
            sum1 += nums[end+1]
            end += 1
        if ans == temp:
            return 0
        return ans

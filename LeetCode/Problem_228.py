# Problem 228: Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        temp = []
        i=0
        while i < len(nums):
            leftVal = nums[i]
            while i < len(nums)-1 and nums[i+1] == nums[i]+1:
                i+=1
            temp.append((leftVal, nums[i]))
            i += 1
       
        result = []
        for (l,r) in temp:
            if l == r:
                result.append(str(l))
            else:
                result.append("%d->%d" % (l,r))
        return result

#Problem 334 - Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
       
        min_till_now = nums[0]
        target = None
        i=1
        while i < len(nums):
            if target != None and nums[i]>target:
                return True
            elif nums[i] > min_till_now:
                target = target if (target != None) and target < nums[i] else nums[i]
                print(target)
            else:
                min_till_now = nums[i]  
            i += 1
        return False

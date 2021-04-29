# Problem 1537 - Get the Maximum Score

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp1 = [0 for i in range(len(nums1)+1)]
        dp2 = [0 for i in range(len(nums2)+1)]
        
        i = len(nums1)-1
        j = len(nums2)-1
        
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]: 
                dp1[i] = nums1[i] + dp1[i+1]
                if nums1[i] == nums2[j]:
                    dp1[i] = max(dp1[i], nums1[i]+dp2[j+1])%1000000007
                    dp2[j] = max(nums2[j]+dp2[j+1], nums1[i]+dp1[i+1])%1000000007
                    j -= 1
                i -= 1
            else:
                dp2[j] = nums2[j] + dp2[j+1]
                if nums1[i] == nums2[j]:
                    dp2[j] = max(dp2[j], nums2[j]+dp1[i+1])%1000000007
                    dp1[i] = max(nums1[i]+dp1[i+1], nums1[i]+dp2[j+1])%1000000007
                    i -= 1
                j -= 1
        
        while i>=0:
            dp1[i] = (nums1[i] + dp1[i+1])%1000000007
            i-=1
        while j>=0:
            dp2[j] = (nums2[j] + dp2[j+1])%1000000007
            j-=1
        
        return max(dp1[0], dp2[0])

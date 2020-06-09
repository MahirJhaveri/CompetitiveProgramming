# 18. 4 Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        # create a hashset to remove duplicates
        ans = set()
       
        # keeps track of the frequency of nums[i] in nums
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1
       
        sum2 = [[0 for i in range(len(nums))] for j in range(len(nums))]
        sum2map = {}
       
        i=0
        while i < len(nums):
            j = i
            while j < len(nums):
                sum2[i][j] = nums[i]+nums[j]
               
                if (target - sum2[i][j]) in sum2map:
                    for tup in sum2map[target - sum2[i][j]]:
                        temp = [nums[i],nums[j],tup[0], tup[1]]
                        temp.sort()
                        ans.add((temp[0],temp[1],temp[2],temp[3]))
               
                if sum2[i][j] not in sum2map:
                    sum2map[sum2[i][j]] = []
                sum2map[sum2[i][j]].append((nums[i],nums[j]))
                j += 1
            i += 1
       
        result = []
       
        for tup in ans:
            temp = {}
            for i in range(4):
                if tup[i] not in temp:
                    temp[tup[i]] = 0
                temp[tup[i]] += 1
            if check(temp, freq):
                result.append([tup[0], tup[1], tup[2], tup[3]])
       
        return result
               
       
def check(ans, freq):
    for each in ans:
        if ans[each] > freq[each]:
            return False
    return True

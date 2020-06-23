# Problem 493: Reverse Pairs

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
       
        if (len(nums) == 0):
            return 0
       
        import math
       
        count = [0]
       
        def modified_merge_sort(nums, start, end, count):
            if start+1 == end:
                return [nums[start]]
            else:
                mid = math.floor((start+end)/2)
                l1 = modified_merge_sort(nums, start, mid, count)
                l2 = modified_merge_sort(nums, mid, end, count)
               
                # incr count
                i=j=0
                while j<len(l2):
                    while i < len(l1) and l1[i] <= 2*l2[j]:
                        i += 1
                    count[0] += len(l1) - i
                    j += 1
               
                # perform merge sort
                i = j = 0
                new_list = []
                while i < len(l1) and j < len(l2):
                    if l1[i] < l2[j]:
                        new_list.append(l1[i])
                        i+=1
                    else:
                        new_list.append(l2[j])
                        j+=1
                while i < len(l1):
                    new_list.append(l1[i])
                    i+=1
                while j < len(l2):
                    new_list.append(l2[j])
                    j+=1
                return new_list
       
        modified_merge_sort(nums, 0, len(nums), count)
        return count[0]

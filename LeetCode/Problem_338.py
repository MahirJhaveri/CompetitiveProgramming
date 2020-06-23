# Problem 338: Counting Bits

class Solution:
    def countBits(self, num: int) -> List[int]:
       
        import math
       
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
       
        max_pow = math.floor(math.log(num, 2))
        print(max_pow)
       
        result=[0,1]
        j=1
        while j < max_pow:
            i=0
            while i < 2 ** (j-1):
                result.append(result[(2 ** (j-1)) + i])
                i += 1
            i=0
            while i < 2 ** (j-1):
                result.append(1 + result[(2 ** (j-1)) + i])
                i += 1
            j += 1
       
        # final part
        if num - 2 ** (max_pow) < 2 ** (max_pow - 1):
            i=0
            while i <= num - 2**(max_pow):
                result.append(result[(2 ** (max_pow-1)) + i])
                i += 1
        else:
            i=0
            while i < 2**(max_pow-1):
                result.append(result[(2 ** (max_pow-1)) + i])
                i += 1
            i=0
            while i <= num - 2**(max_pow) - 2**(max_pow-1):
                result.append(1 + result[(2 ** (max_pow-1)) + i])
                i += 1
        return result

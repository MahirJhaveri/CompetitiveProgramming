# Problem 134 - Gas Station

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        diffs = [0 for x in range(len(gas))]
        
        s = 0
        for i in range(len(gas)):
            diffs[i] = gas[i] - cost[i]
            s += diffs[i]
            
        if s < 0: return -1
        
        start = 0
        pos = 0
        s = 0
        while pos < len(gas):
            s += diffs[pos]
            pos += 1
            if s < 0:
                start = pos
                s = 0
        return start

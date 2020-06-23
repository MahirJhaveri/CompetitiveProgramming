# Problem 895. Maximum Frequency Stack

import collections

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = collections.defaultdict(list)
        self.maxfreq = 0  

    def push(self, x: int) -> None:
        f = self.freq.get(x, 0) + 1
        self.freq[x] = f
        self.group[f].append(x)
        self.maxfreq = f if self.maxfreq < f else self.maxfreq
       

    def pop(self) -> int:
        if self.maxfreq <= 0:
            return None
       
        ans = self.group[self.maxfreq].pop()
        self.freq[ans] -= 1
        while self.maxfreq > 0 and len(self.group[self.maxfreq]) == 0:
            self.maxfreq -= 1
        return ans

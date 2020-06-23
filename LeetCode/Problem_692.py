# Problem 692: Top K frequent words

class Solution:
   
    # Can be done in 2 ways:
    # 1) By sorting (nlogn)
    # 2) By using heaps (nlogk)
       
   
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
       
        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 0
            hashmap[word] += 1
       
        # min heap
        heap = []
       
        # inserts an element into the heap
        def insert(element, heap):
            heap.append(element)
            pos = len(heap)-1
            while pos >= 0:
                ppos = int((pos-1)/2)
                if heap[ppos][1] > heap[pos][1]:
                    temp = heap[ppos]
                    heap[ppos] = heap[pos]
                    heap[pos] = temp
                elif heap[ppos][1] == heap[pos][1] and heap[ppos][0] < heap[pos][0]:
                    temp = heap[ppos]
                    heap[ppos] = heap[pos]
                    heap[pos] = temp
                else:
                    break
                pos = ppos
       
        def pop(heap):
            if len(heap) == 0:
                return None
            elif len(heap) == 1:
                return heap.pop()
           
            top = heap[0]
            last = heap.pop()
            heap[0] = last
            pos = 0
            while pos < len(heap):
                lcpos = 2*pos+1
                rcpos = 2*pos+2
                if lcpos >= len(heap):
                    break
                elif rcpos >= len(heap):
                    if heap[pos][1] > heap[lcpos][1] or (heap[pos][1] == heap[lcpos][1] and heap[pos][0] < heap[lcpos][0]):
                        temp = heap[lcpos]
                        heap[lcpos] = heap[pos]
                        heap[pos] = temp
                    break
                else:
                    if heap[rcpos][1] < heap[lcpos][1] or (heap[rcpos][1] == heap[lcpos][1] and heap[rcpos][0] > heap[lcpos][0]):
                        mcpos = rcpos
                    else:
                        mcpos = lcpos
                    if heap[pos][1] > heap[mcpos][1] or (heap[pos][1] == heap[mcpos][1] and heap[pos][0] < heap[mcpos][0]):
                        temp = heap[mcpos]
                        heap[mcpos] = heap[pos]
                        heap[pos] = temp
                        pos = mcpos
                    else:
                        break
           
            return top
       
        for word in hashmap.keys():
            insert((word, hashmap[word]), heap)
            if len(heap) > k:
                pop(heap)
       
        temp = []
        i=0
        while i < k:
            temp.append(pop(heap))
            i+=1
        temp.reverse()
        return map(lambda tup: tup[0], temp)

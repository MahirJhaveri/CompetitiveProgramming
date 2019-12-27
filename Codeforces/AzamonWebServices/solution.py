# 1281B - Azamon Web Services


# Dictionary + linked list
# Check presence - O(1)
# Deletion - O(1)
# Get min - O(1)


class OrderedDict:

    class Node:
        def __init__(self, val, pos):
            self.val = val
            self.pos = pos
            self.prev = None
            self.next = None

    def __init__(self, l):
        lst = [(l[c], c) for c in range(len(l))]
        lst.sort(key=lambda tup: tup[1], reverse=True)
        lst.sort(key=lambda tup: tup[0])
        # print(lst)
        self.hashmap = {}
        self.start = self.Node("Start", None)
        self.end = self.Node("end", None)
        cur = self.start
        for tup in lst:
            char = tup[0]
            pos = tup[1]
            node = self.Node(char, pos)
            cur.next = node
            node.prev = cur
            cur = node

            # hashmap has pointers to corresponding nodes in dll
            if char not in self.hashmap:
                self.hashmap[char] = {}
            self.hashmap[char][pos] = node
        cur.next = self.end
        self.end.prev = cur

    def get_min(self):
        node = self.start.next
        if node == self.end:
            return None, None
        else:
            return node.val, node.pos

    def delete(self, char, pos):
        if char not in self.hashmap:
            return None, None
        elif pos not in self.hashmap[char]:
            return None, None
        else:
            node = self.hashmap[char][pos]
            self.hashmap[char].pop(pos)
            if len(self.hashmap[char]) == 0:
                self.hashmap.pop(char)
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return node.val, node.pos

    def is_present(self, e):
        return e in self.hashmap


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


T = int(input())
for t in range(T):
    [word1, word2] = input().rstrip().split()
    lst1 = list(word1)
    lst2 = list(word2)
    od = OrderedDict(lst1)
    # for node in od.hashmap['A']:
    #print((node.val, node.pos))

    num_swaps = 0
    Impossible = False

    i = 0
    while i < min(len(lst1), len(lst2)):
        if lst1[i] > lst2[i]:
            if num_swaps == 1:
                Impossible = True
                break
            else:
                (min_char, min_pos) = od.get_min()
                if min_char > lst2[i]:
                    Impossible = True
                    break
                else:
                    swap(lst1, i, min_pos)
                    num_swaps += 1
                    od.delete(min_char, min_pos)
                    if min_char < lst2[i]:
                        break
        elif lst1[i] == lst2[i]:
            if num_swaps == 1:
                od.delete(lst1[i], i)
            else:
                (min_char, min_pos) = od.get_min()
                if min_char >= lst2[i]:
                    od.delete(lst1[i], i)
                else:
                    swap(lst1, i, min_pos)
                    num_swaps += 1
                    od.delete(min_char, min_pos)
                    if min_char < lst2[i]:
                        break
        else:
            break
        i += 1

    if i == min(len(lst1), len(lst2)) and lst1[i-1] == lst2[i-1]:
        Impossible = True if len(lst1) >= len(lst2) else False

    if Impossible == True:
        print("---")
    else:
        print("".join(lst1))

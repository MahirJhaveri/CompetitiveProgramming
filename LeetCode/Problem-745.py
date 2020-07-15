# Problem 745: Prefix and Suffix Search

class WordFilter(object):

    def __init__(self, words):
        self.trie = {
            "val":-1
        }
        for i in range(len(words)):
            start = 0
            words[i] = words[i] + "#"
            while start < len(words[i]):
                word =  words[i][start:len(words[i])] + words[i][0:-1]
                # insert word into trie with value = i
                print(word)
                node = self.trie
                for char in word:
                    if char not in node:
                        node[char] = {
                            "val":i
                        }
                    else:
                        node[char]["val"] = i
                    node = node[char]
                start += 1
        

    def f(self, prefix, suffix):
        temp = suffix + "#"+ prefix
        node = self.trie
        i = 0
        while i < len(temp) and temp[i] in node:
            node = node[temp[i]]
            i += 1
        if i == len(temp):
            return node["val"]
        else:
            return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

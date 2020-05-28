# Word search II

class Solution(object):
    
    def findWords(self, board, words):
        
        # first add all words to the trie
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        #print(trie.root.next)
        
        result = {}
        row = 0
        while row < len(board):
            col = 0
            while col < len(board[0]):
                marker = Marker(len(board[0]), len(board))
                trie.reset()
                analyze(row, col, board, trie, result, marker)
                col += 1
            row += 1
        
        return result.keys()

def analyze(row, col, board, trie, result, marker):
    if not marker.is_marked(row, col):
        if trie.check_char(board[row][col]):
            marker.mark(row, col)
            trie.add_char(board[row][col])
            
            if trie.check_done():
                result[trie.curr.done] = True
            
            neighbors = get_neighbors(row, col, board)
            for (rn, cn) in neighbors:
                analyze(rn, cn, board, trie, result, marker)
            
            marker.unmark(row, col)
            trie.backtrack()
            
        
# returns all the valid neighbors of (row, col)
def get_neighbors(row, col, board):
    result = []
    #(row-1,col)
    if row > 0:
        result.append((row-1,col))
    
    # (row, col-1):
    if col > 0:
        result.append((row, col-1))
    
    # (row+1,col)
    if row < len(board)-1:
        result.append((row+1,col))
    
    # (row, col+1)
    if col < len(board[0])-1:
        result.append((row,col+1))
    
    return result

class Trie:  
    class Node:
        def __init__(self, done, prev):
            self.done = done
            self.next = {}
            self.prev = prev
    
    def __init__(self):
        self.root = self.Node(None, None)
        self.curr = self.root
    
    # add a word to the trie
    def add_word(self, word):
        self.curr = self.root
        for char in word:
            if char in self.curr.next:
                self.curr = self.curr.next[char]
            else:
                self.curr.next[char] = self.Node(None, self.curr)
                self.curr = self.curr.next[char]
        self.curr.done = word
    
    # check if there is any path from current node with char
    def check_char(self, char):
        return char in self.curr.next
    
    # check is some word ends at the given node
    def check_done(self):
        return self.curr.done != None
    
    # add char and move to the next state
    # only use this after making sure that char is in the trie
    def add_char(self,char):
        self.curr = self.curr.next[char]
    
    # Take a step back and jump back to the parent
    def backtrack(self):
        self.curr = self.curr.prev
    
    # resets the curr node
    def reset(self):
        self.curr = self.root
        
        
# Build a trie from the dictionary words
# how will you use the try?
# --> Convert board to graph
# --> traverse every node and see if you find a match in the trie, use recursive backtracking



# Marker class for backtracking
class Marker:
    def __init__(self, num_cols, num_rows):
        self.marker = {}
        self.num_cols = num_cols
        row = 0
        while row < num_rows:
            col = 0
            while col < num_cols:
                self.marker[row*num_cols + col] = False
                col += 1
            row += 1
    
    # mark (row, col)
    def mark(self, row, col):
        temp = row*self.num_cols + col
        self.marker[temp] = True

    # check if (row, col) has been visited
    def is_marked(self, row, col):
        temp = row*self.num_cols + col
        return self.marker[temp]
    
    # unmark (row, col)
    def unmark(self, row, col):
        temp = row*self.num_cols + col
        self.marker[temp] = False

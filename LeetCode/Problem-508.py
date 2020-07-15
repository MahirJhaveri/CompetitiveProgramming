# Problem 508: Most frequent subtree sub

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        c=defaultdict(lambda: 0, {})
       
        def aux(root):
            if root == None:
                return 0, [], 0
            else:
                sl, ansl, ansfl = aux(root.left)
                sr, ansr, ansfr = aux(root.right)
               
                c[root.val+sl+sr] += 1
               
                if ansfl == ansfr:
                    ans = ansl + ansr
                    ansf = ansfl
                elif ansfl>ansfr:
                    ans, ansf = ansl, ansfl
                else:
                    ans, ansf = ansr, ansfr
               
                if c[root.val+sl+sr] == ansf:
                    ans.append(root.val+sl+sr)
                elif ansf>c[root.val+sl+sr]:
                    ans, ansf = ans, ansf
                else:
                    ans, ansf = [root.val+sl+sr], c[root.val+sl+sr]
               
                return root.val+sl+sr, ans, ansf
       
        _,ans,_ = aux(root)
        return ans 

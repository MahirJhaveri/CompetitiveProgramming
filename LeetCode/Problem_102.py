# Problem 102: Binary Tree Level Order Traversal

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = []
        levelOrderAux(root, 0, result)
        return result
       
def levelOrderAux(root, depth, result):
    if len(result) <= depth:
        result.append([])
    result[depth].append(root.val)
    if root.left:
        levelOrderAux(root.left, depth+1,result)
    if root.right:
        levelOrderAux(root.right, depth+1,result)

# Problem 117: Populating Next Right Pointers in Each Node II

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        closestAux(root, None)
        return root

def closestAux(node, imRight):
    node.next = imRight
   
    while imRight != None and imRight.left == None and imRight.right == None:
        imRight = imRight.next
   
    imRightRight = None
    if imRight and imRight.left:
        imRightRight = imRight.left
    elif imRight and imRight.right:
        imRightRight = imRight.right
   
    if node.right:
        closestAux(node.right, imRightRight)
        if node.left:
            closestAux(node.left, node.right)
    else:
        if node.left:
            closestAux(node.left, imRightRight)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftvalidity = rightvalidity = True
        
        if root.left:
            x = self.leftmax(root.left)
            leftvalidity = self.isValidBST(root.left) and root.val > x

        if root.right:
            y = self.rightmin(root.right)
            rightvalidity = self.isValidBST(root.right) and root.val < y
        
        # print(leftvalidity, rightvalidity)
        return leftvalidity and rightvalidity
    
    def leftmax(self, root) -> TreeNode:
        if root.left == None and root.right == None:
            return root.val
        else:
            if root.left and root.right:
                return max(root.val, self.leftmax(root.left), self.leftmax(root.right))
            elif root.left:
                return max(root.val, self.leftmax(root.left))
            else:
                return max(root.val, self.leftmax(root.right))
    
    def rightmin(self, root) -> TreeNode:
        if root.left == None and root.right == None:
            return root.val
        else:
            if root.left and root.right:
                return min(root.val, self.rightmin(root.left), self.rightmin(root.right))
            elif root.left:
                return min(root.val, self.rightmin(root.left))
            else:
                return min(root.val, self.rightmin(root.right))
                
            
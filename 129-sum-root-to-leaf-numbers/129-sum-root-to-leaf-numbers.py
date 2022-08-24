# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def dfs(node, num):
            if not node:
                return
            if not node.left and not node.right:
                num += str(node.val)
                nums.append(int(num))

            num+= str(node.val)
            dfs(node.left, num)
            dfs(node.right, num)
            
        dfs(root, "")
        return sum(nums)
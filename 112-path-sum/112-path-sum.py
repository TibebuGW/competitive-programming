# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(head, count):
            # count += head.val
            if head.left == head.right == None:
                if count + head.val == targetSum:
                    return True
                else:
                    return False
             
            temp = False
            if head.left:
                # count += head.val
                temp = temp or dfs(head.left, count + head.val)
            if head.right:
                # count += head.val
                temp = temp or dfs(head.right, count + head.val)
                
            # print(head.val, count)
            # count -= head.val
                
            return temp
        
        c = 0
        if root == None:
            return False
        else:
            return dfs(root, c)
        
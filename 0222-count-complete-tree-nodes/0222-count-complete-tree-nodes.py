# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def depthCounter(node):
            if not node:
                return 0
            return 1 + depthCounter(node.left)
        
        depth = depthCounter(root)
        
        
        
        
        def dfs(node, left_end, right_end, index):
            if not node:
                return False
            
            if left_end == right_end:
                return True
            
            mid = (left_end+right_end)//2
            if index <= mid:
                return dfs(node.left, left_end, mid, index)
            else:
                return dfs(node.right, mid+1, right_end, index)
            
            
        best = -1
        l = 0
        r = (2**(depth-1))-1
        left = 0
        right = (2**(depth-1))-1
        count = right
        while left <= right:
            mid = (left+right)//2
            mid_value = dfs(root, l, r, mid)
            if mid_value:
                left = mid+1
                best = mid
            else:
                right = mid-1
        return count + best + 1
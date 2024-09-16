# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 1
        
        while queue:
            
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level
            
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            level += 1
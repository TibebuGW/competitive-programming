# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        
        queue = deque([(root, 0)])

        level = 0
        while queue:
            length = len(queue)
            level += 1
            l = -1
            r = len(queue)
            i = 0
            j = 0
            while i < length:
                node, index = queue.popleft()
                        
                if node.left:
                    if l == -1:
                        l = index * 2
                    r = index * 2
                    queue.append((node.left, index * 2))
                    
                if node.right:
                    if l == -1:
                        l = (index * 2) + 1
                    r = (index * 2) + 1
                    queue.append((node.right, (index * 2) + 1))
                
                
                j += 2
                i += 1
            if l != -1:
                ans = max(ans, r - l + 1)
            
        
        return ans
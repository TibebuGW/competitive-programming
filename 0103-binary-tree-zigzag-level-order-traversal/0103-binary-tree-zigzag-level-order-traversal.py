# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level = 0
        ans = []
        
        while queue:
            n = len(queue)
            temp_arr = []
            for _ in range(n):
                node = queue.popleft()
                temp_arr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level % 2 == 0:
                ans.append(temp_arr)
            else:
                ans.append(temp_arr[::-1])
                
            level += 1
        
        return ans
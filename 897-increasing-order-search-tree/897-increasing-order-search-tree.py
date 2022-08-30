# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return ""
            return "-".join([dfs(node.left), str(node.val), dfs(node.right)])
        
        s = dfs(root).split("-")
        # print(s)
        head = temp = TreeNode()
        for char in s:
            if char != '':
                temp.right = TreeNode(int(char))
                temp = temp.right
            
        return head.right
            
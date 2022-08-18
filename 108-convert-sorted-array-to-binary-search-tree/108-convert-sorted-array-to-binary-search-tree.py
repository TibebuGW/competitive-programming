# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        visited = set()
        def dfs(arr, left, right):
            nonlocal visited
            mid = (left+right)//2
            if mid in visited:
                return None
            else:
                visited.add(mid)
                # print(visited)
                leftChild = dfs(arr, left, mid)
                rightChild = dfs(arr, mid+1, right)
                return TreeNode(arr[mid], leftChild, rightChild)
        
        return dfs(nums, 0, len(nums)-1)
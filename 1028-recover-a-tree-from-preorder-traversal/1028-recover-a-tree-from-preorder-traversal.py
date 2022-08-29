# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        arr = traversal.split("-")
        root = TreeNode(int(arr[0]))
        d = defaultdict(list)
        d[0].append(root)
        left = len(arr[0])
        right = left+1
        # print("first", left, right)
        
        while right < len(traversal):
            if traversal[right] == "-":
                right += 1
            else:
                level = right-left
                num = []
                # print("right:", right)
                while right < len(traversal) and traversal[right] != "-":
                    num.append(traversal[right])
                    right += 1
                nodeValue = int("".join(num))
                node = TreeNode(nodeValue)
                d[level].append(node)
                parent = d[level-1][-1]
                if parent.left:
                    parent.right = node
                else:
                    parent.left = node
                
                left = right
                right += 1
        
        return root
                
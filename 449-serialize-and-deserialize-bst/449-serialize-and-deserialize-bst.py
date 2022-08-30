# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []
        
        def dfs(node, level, side):
            nonlocal arr
            if not node:
                return
            
            component = "*"*level + str(node.val) + side
            arr.append(component)
            dfs(node.left, level+1, "l")
            dfs(node.right, level+1, "r")
        
        dfs(root, 0,"r")
        
        return "".join(arr)
        
    def deserialize(self, traversal):
        # print(traversal)
        if not traversal:
            return
        arr = traversal.split("*")
        root = TreeNode(int(arr[0][:-1]))
        d = defaultdict(list)
        d[0].append(root)
        left = len(arr[0])
        right = left+1
        # print("first", left, right)
        last = "right"
        while right < len(traversal):
            if traversal[right] == "*":
                right += 1
            else:
                level = right-left
                num = []
                # print("right:", right)
                while right < len(traversal) and traversal[right] != "*":
                    num.append(traversal[right])
                    right += 1
                # print("here:","".join(num[:-1]))
                side = num[-1]
                nodeValue = int("".join(num[:-1]))
                node = TreeNode(nodeValue)
                d[level].append(node)
                # print(nodeValue)
                parent = d[level-1][-1]
                if side == "r":
                    parent.right = node
                else:
                    parent.left = node
                
                left = right
                right += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
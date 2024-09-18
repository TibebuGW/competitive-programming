# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []
        def dfs(node = root):
            if not node:
                ans.append("N")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs()
        return "#".join(ans)

    def deserialize(self, data):
        values = data.split("#")
        i = 0
        def dfs():
            nonlocal i
            if values[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(values[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
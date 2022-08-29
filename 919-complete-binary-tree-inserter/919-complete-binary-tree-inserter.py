# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque([root])
        
        while True:
            if self.queue[0].left and self.queue[0].right:
                self.queue.append(self.queue[0].left)
                self.queue.append(self.queue[0].right)
                self.queue.popleft()
            else:
                if self.queue[0].left:
                    self.queue.append(self.queue[0].left)
                    self.last = "left"
                else:
                    self.last = "right"
                break
        
        self.head = root

    def insert(self, val: int) -> int:
        if self.last == "right":
            newNode = TreeNode(val)
            self.queue[0].left = newNode
            self.last = "left"
            self.queue.append(newNode)
            return self.queue[0].val
        else:
            newNode = TreeNode(val)
            self.queue[0].right = newNode
            self.last = "right"
            self.queue.append(newNode)
            parent = self.queue.popleft()
            return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.head


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
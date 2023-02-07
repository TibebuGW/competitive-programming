from random import choices
class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.list = w
        self.length = len(w)
        self.prob = [self.list[i]/self.total for i in range(self.length)]
        self.indices = [i for i in range(self.length)]

    def pickIndex(self) -> int:
        return choices(self.indices, self.prob)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class RecentCounter:

    def __init__(self):
        self.nums = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.nums.append(t)
        x = 0
        while t - 3000 > self.nums[0]:
            self.nums.pop(0)

        return len(self.nums)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

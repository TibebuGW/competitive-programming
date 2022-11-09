class StockSpanner:

    def __init__(self):
        self.prices = []
        self.ans = []
        self.stack = []
        
    def next(self, price: int) -> int:
        self.prices.append(price)
        cur_ans = 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            index = self.stack.pop()
            cur_ans += self.ans[index]
        self.stack.append(len(self.prices)-1)
        self.ans.append(cur_ans)
        return self.ans[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
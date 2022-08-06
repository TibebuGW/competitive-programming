class HistoryNode:
    def __init__(self, homepage="", back=None, forward=None):
        self.homepage = homepage
        self.back = back
        self.forward = forward
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        self.new = HistoryNode(url, None, None)
        self.current.forward = self.new
        self.temp = self.current
        self.current = self.new
        self.current.back = self.temp

    def back(self, steps: int) -> str:
        while steps and self.current.back:
            self.current = self.current.back
            steps -= 1
        return self.current.homepage

    def forward(self, steps: int) -> str:
        while steps and self.current.forward:
            self.current = self.current.forward
            steps -= 1
        return self.current.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
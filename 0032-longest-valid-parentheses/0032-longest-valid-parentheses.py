class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = deque([])
        ans = 0
        
        for index, char in enumerate(s):
            if char == "(":
                queue.append((index, char))
            else:
                if queue and queue[-1][1] == "(":
                    queue.pop()
                else:
                    queue.append((index, char))
        
        queue.appendleft((-1, ""))
        queue.append((len(s), ""))
        
        for i in range(1, len(queue)):
            ans = max(ans, queue[i][0] - queue[i - 1][0] - 1)
        
        return ans
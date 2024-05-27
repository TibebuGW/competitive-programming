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
        
        if not queue or queue[0][0] != 0:
            queue.appendleft((-1, ""))
        
        if not queue or queue[-1][0] != len(s) - 1:
            queue.append((len(s), ""))
        
        for i in range(1, len(queue)):
            ans = max(ans, queue[i][0] - queue[i - 1][0] - 1)
        
        return ans
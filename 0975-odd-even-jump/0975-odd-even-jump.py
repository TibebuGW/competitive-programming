class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        next_greater = [-1 for _ in range(len(arr))] 
        next_smaller = [-1 for _ in range(len(arr))]
        dp = [[False, False] for _ in range(len(arr))]
        dp[-1] = [True, True]
        
        # Find the next least greater element
        max_stack = [] # decreasing monotonic stack
        min_stack = [] # decreasing monotonic stack
        index_element_list = [(ele, ind) for ind, ele in enumerate(arr)]
        inc_sorted = [ele[1] for ele in sorted(index_element_list)]
        dec_sorted = sorted(inc_sorted, key=lambda x: arr[x], reverse=True)
        
        for i in range(len(arr)):
            while min_stack and inc_sorted[min_stack[-1]] < inc_sorted[i]:
                idx = min_stack.pop()
                next_greater[inc_sorted[idx]] = inc_sorted[i]
            min_stack.append(i)
        
        for i in range(len(arr)):
            while max_stack and dec_sorted[max_stack[-1]] < dec_sorted[i]:
                idx = max_stack.pop()
                next_smaller[dec_sorted[idx]] = dec_sorted[i]
            max_stack.append(i)
        
        for i in range(len(arr) - 2, -1, -1):
            if next_greater[i] != -1 and dp[next_greater[i]][1]:
                dp[i][0] = True
            
            if next_smaller[i] != -1 and dp[next_smaller[i]][0]:
                dp[i][1] = True
        
        count = 0
        for i in range(len(arr)):
            if dp[i][0]:
                count += 1
                
        return count
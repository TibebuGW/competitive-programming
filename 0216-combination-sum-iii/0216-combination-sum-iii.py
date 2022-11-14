class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def backtrack(count, total_so_far, path, index):
            if count == k:
                if total_so_far == n:
                    ans.append(path[::])
                return 
            
            
            for num in range(index, 10):
                if total_so_far + num <= n:
                    path.append(num)
                    total_so_far += num
                    backtrack(count + 1, total_so_far, path, num+1)
                    path.pop()
                    total_so_far -= num
                else:
                    break
        
        backtrack(0, 0, [], 1)
        return ans
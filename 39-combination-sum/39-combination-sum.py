class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def dfs(node, path, total):
            for num in candidates:
                if num >= node:
                    if total + num == target:
                        ans.append(path+[num])
                        break
                    elif total + num > target:
                        return
                    else:
                        path.append(num)
                        total += num
                        dfs(num, path, total)
                        path.pop()
                        total -= num

        
        
        for num in candidates:
            if num < target:
                dfs(num, [num], num)
                
            elif num == target:
                ans.append([num])
                break
            else:
                break
            
        return ans
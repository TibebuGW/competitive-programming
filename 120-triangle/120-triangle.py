class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = [[0]*10]*len(triangle)
        dp = []
        for i in range(1,len(triangle)+1):
            dp.append([0]*i)
        
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    dp[i][j] = triangle[i][j]
                    # print(dp[i])
                    continue
                    
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                
            # print(dp[i])
                    
        # print(dp)
        
        return min(dp[-1])
                    
                
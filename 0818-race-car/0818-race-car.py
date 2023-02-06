class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        
        for i in range(1, target + 1):
            forward = 1
            while (1 << forward) - 1 < 2 * i:
                j = (1 << forward) - 1
                if i == j:
                    dp[i] = forward  
                elif i > j:
                    for back in range(forward):
                        k = (1 << back) - 1
                        dp[i] = min(dp[i], forward + 1 + back + 1 + dp[i - j + k]) 
                else:
                    dp[i] = min(dp[i], forward + 1 + dp[j - i])  
                
                forward += 1
        
        return dp[target]
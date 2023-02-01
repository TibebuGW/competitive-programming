class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        main_array = []
        for i in range(n):
            main_array.append([ages[i], scores[i]])
        main_array.sort()
        
        memo = {}
        def dp(cur_index = 0, min_age_index = -1):
            
            if (cur_index, min_age_index) in memo:
                return memo[(cur_index, min_age_index)]
            
            if cur_index == n:
                memo[(cur_index, min_age_index)] = 0
                return memo[(cur_index, min_age_index)]
            
            not_take = dp(cur_index + 1, min_age_index)
            take = 0
            if min_age_index == -1 or main_array[min_age_index][1] <= main_array[cur_index][1]:
                take = main_array[cur_index][1] + dp(cur_index + 1, cur_index)
            
            
            memo[(cur_index, min_age_index)] = max(take, not_take)
            return memo[(cur_index, min_age_index)]        
        return dp()

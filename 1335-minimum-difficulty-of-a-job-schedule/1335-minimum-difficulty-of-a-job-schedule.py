class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def solve(index, day):
            if day == 1:
                max_ = -1
                for i in range(index, len(jobDifficulty)):
                    if jobDifficulty[i] > max_:
                        max_ = jobDifficulty[i]
                return max_
            else:
                max_ = -1
                res = float('inf')
                for i in range(index, len(jobDifficulty)-(day-1)):
                    if jobDifficulty[i] > max_:
                        max_ = jobDifficulty[i]
                    res = min(res, max_ + solve(i+1, day-1))
                    # print(res)
                return res
            
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)
        else:
            return solve(0, d)
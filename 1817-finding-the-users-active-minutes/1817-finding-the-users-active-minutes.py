class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_to_UAM = defaultdict(set)
        for user, minute in logs:
            user_to_UAM[user].add(minute)
        
        UAM_count = defaultdict(int)
        for key, val in user_to_UAM.items():
            UAM_count[len(val)] += 1
        
        ans = []
        for j in range(1, k + 1):
            ans.append(UAM_count[j])
        
        return ans
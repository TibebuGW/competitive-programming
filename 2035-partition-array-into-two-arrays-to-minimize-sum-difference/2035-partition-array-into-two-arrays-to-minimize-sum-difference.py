class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m//2
        dict_A = defaultdict(set)
        dict_B = defaultdict(set)
        first_part = nums[:n]
        second_part = nums[n:]
        total_sum = sum(nums)
        goal = total_sum/2
        
        for k in range(n + 1):
            dict_A[k] = set(map(sum, combinations(first_part, k)))
            dict_B[k] = set(map(sum, combinations(second_part, k)))
            
        for key, val in dict_B.items():
            dict_B[key] = list(val)
            dict_B[key].sort()
        
        ans = float('inf')
        
        for first_key, first_list in dict_A.items():
            for first_list_number in first_list:
                num_to_search = goal - first_list_number
                l = 0
                r = len(dict_B[n - first_key]) - 1
                best = -1
                if first_key == n and first_list_number == goal:
                    return 0
                while l <= r:
                    mid = (l + r)//2
                    if first_key == 0 and dict_B[n][mid] == goal:
                        return 0
                    if dict_B[n - first_key][mid] < num_to_search:
                        best = mid
                        l = mid + 1
                    elif dict_B[n - first_key][mid] > num_to_search:
                        r = mid - 1
                    else:
                        best = mid
                        break
                        
                second_list_number = 0
                if best == - 1:
                    second_list_number = dict_B[n - first_key][0]
                elif 0 <= best < len(dict_B[n - first_key]) - 1:
                    if num_to_search - dict_B[n - first_key][best] < dict_B[n - first_key][best + 1] - num_to_search:
                        second_list_number = dict_B[n - first_key][best]
                    else:
                        second_list_number = dict_B[n - first_key][best + 1]
                else:
                    second_list_number = dict_B[n - first_key][-1]
                
                candidate = first_list_number + second_list_number
                # print(candidate)
                if candidate == goal:
                    return 0
                if abs(goal - candidate) < abs(goal - ans):
                    ans = candidate
        
        return abs(ans - (total_sum - ans))
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        length = -1
        initial = total = 0
        for pos, amount in fruits:
            length = max(length, pos)
            if pos == startPos:
                initial = total = amount
        main = [0]*(length+1)
        left = [0]*(startPos)
        right = [0]*((length-startPos))
        
        for pos, amount in fruits:
            main[pos] = amount
            if pos < startPos:
                left[startPos-pos-1] = amount
            elif pos > startPos:
                right[pos-startPos-1] = amount
        
        # print(main)
        # print(left)
        # print(right)
        
        left = list(accumulate(left)) if len(list(accumulate(left))) else [0]
        right = list(accumulate(right)) if len(list(accumulate(right))) else [0]
        # print(right)
        
        for i in range(len(left)):
            left_steps = i+1
            right_steps = k-(2*(left_steps)) if k-(2*(left_steps)) > 0 else 0
            if right_steps > 0:
                if (left_steps*2)+right_steps <= k:
                    
                    if right_steps > len(right)-1:
                        # print("first loop 1", left[left_steps-1]+initial)
                        total = max(total, left[left_steps-1]+right[-1]+initial)
                    else:
                        # print("first loop 2", left[left_steps-1]+right[right_steps-1]+initial)
                        total = max(total, left[left_steps-1]+right[right_steps-1]+initial)
                else:
                    break
            else:
                if left_steps <= k:
                    # print("first loop 3", left[left_steps-1]+initial)
                    total = max(total, left[left_steps-1]+initial)
                else:
                    break
        
        for i in range(len(right)):
            right_steps = i+1
            left_steps = k-(2*(right_steps)) if k-(2*(right_steps)) > 0 else 0
            if left_steps:
                if left_steps+(right_steps)*2 <= k:
                    if left_steps > len(left)-1:
                        # print("second loop 1", right[right_steps-1]+initial)
                        total = max(total, right[right_steps-1]+left[-1]+initial)
                    else:
                        # print("second loop 2", left[left_steps-1]+right[right_steps-1]+initial)
                        total = max(total, left[left_steps-1]+right[right_steps-1]+initial)
                else:
                    break
            else:
                if right_steps <= k:
                    # print("second loop 3", right[right_steps-1]+initial)
                    total = max(total, right[right_steps-1]+initial)
                else:
                    break
        
        return total
        
        
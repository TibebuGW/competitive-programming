class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1]*n
        stack = []
        
        for i in range(n-1, -1, -1):
            cur_car_position, cur_car_speed = cars[i]
            
            while stack and (stack[-1][1] >= cur_car_speed or (stack[-1][0] - cur_car_position)/(cur_car_speed-stack[-1][1]) > stack[-1][2]):
                stack.pop()
            
            if not stack:
                stack.append((cur_car_position, cur_car_speed, float('inf')))
            else:
                ans[i] = (stack[-1][0] - cur_car_position)/(cur_car_speed-stack[-1][1])
                stack.append((cur_car_position, cur_car_speed, ans[i]))
        
        return ans
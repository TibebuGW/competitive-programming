class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars.sort()
        stack = []
        print(cars)
        # (1, 1), (2, 2), (3, 1) 4
        
        for car in cars:
            cur_car_position, cur_car_speed = car
            
            while stack and stack[-1][1] > cur_car_speed:
                time = (cur_car_position - stack[-1][0])/(stack[-1][1] - cur_car_speed)
                collision_pos = cur_car_position + (time * cur_car_speed)
                
                if collision_pos <= target:
                    stack.pop()
                else:
                    break
            
            stack.append((cur_car_position, cur_car_speed))
        
        return len(stack)
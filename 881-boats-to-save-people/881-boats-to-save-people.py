class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        left = 0
        right = len(people)-1
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                result += 1
                left += 1
                right -= 1
            else:
                result += 1
                right -=1
            
        return result
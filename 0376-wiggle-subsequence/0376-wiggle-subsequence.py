class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        total = len(nums)
        deductable = 0
        signs_array = []
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] < 0:
                signs_array.append("-")
            elif nums[i]-nums[i-1] > 0:
                signs_array.append("+")
            else:
                deductable += 1        
        if len(signs_array) == 1:
            if signs_array[0] == "+" or signs_array[0] == "-":
                return 2
            else:
                return 1
        else:
            left_pointer = 0
            right_pointer = 1
            while right_pointer < len(signs_array):
                while right_pointer < len(signs_array) and signs_array[left_pointer] == signs_array[right_pointer]:
                    right_pointer += 1
                
                deductable += (right_pointer-left_pointer-1)
                
                left_pointer = right_pointer
                right_pointer += 1
                
            
            total -= deductable
            return total
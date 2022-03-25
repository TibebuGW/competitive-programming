class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        i=0
        ans=0
        
        while i<len(nums):
            minheap=[]
            maxheap=[]
            j=i
            while j <len(nums):
                heappush(minheap,nums[j])
                heappush(maxheap,-nums[j])
                ans+=-maxheap[0]-minheap[0]
                j+=1    
            i+=1
            
        return ans    
                    
                
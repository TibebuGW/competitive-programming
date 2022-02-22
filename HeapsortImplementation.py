class Solution:
    def left_child(self, index):
        return 2*index+1
        
    def right_child(self, index):
        return 2*index+2
        
    def heapify(self,arr, n, i):
        # code here
        smallest = i
        l = self.left_child(i)
        r = self.right_child(i)
        
        if l < n and arr[smallest] < arr[l]:
            smallest = l
        
        if r < n and arr[smallest] < arr[r]:
            smallest = r
            
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.heapify(arr, n, smallest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        last_node = (n//2)-1
        
        for i in range(last_node, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        # print(arr)
        r = n-1 
        while r>0:
            arr[0], arr[r] = arr[r], arr[0]
            self.heapify(arr, r, 0)
            r-=1

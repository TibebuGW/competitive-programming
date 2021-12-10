selectionSort(arr,n){
   //code here
   var j, min, temp
   for(let i = 0; i < arr.length; i++){
       j = i + 1
       min = i
       for(j; j < arr.length; j++){
           if(arr[j] < arr[min]){
               min = j
           }
       }
       temp = arr[min]
       arr[min] = arr[i]
       arr[i] = temp
   }
}

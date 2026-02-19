def prefix_sum_(arr,i=1):
    if (i>=len(arr)):
        return arr
    arr[i] = arr[i-1]+arr[i]
    return prefix_sum_(arr,i+1)

arr=[2,4,6,8,10]
result=prefix_sum_(arr)
print(result)
    
 

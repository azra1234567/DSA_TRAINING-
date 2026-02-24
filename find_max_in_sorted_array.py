def findMax(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        if arr[low] <= arr[high]:
            return arr[high]
        mid = low + (high - low) // 2
        low = mid
        else:
            high = mid - 1
        return arr[low]
    arr = [7, 8, 9, 10, 1, 2, 3, 4, 5]
print(findMax(arr))
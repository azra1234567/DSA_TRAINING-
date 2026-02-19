arr=[2,4,6,8,10]
def prefix_sum_array(nums):
prefix_sums = []
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sums.append(current_sum)
    return prefix_sums
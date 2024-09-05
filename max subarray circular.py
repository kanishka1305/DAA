def maxSubarraySumCircular(nums):
    total_sum = max_sum = min_sum = curr_max = curr_min = nums[0]
    
    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
        
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)
        
        total_sum += num
    
    return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum

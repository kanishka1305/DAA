def rob_houses(nums):
    if len(nums) == 1:
        return nums[0]
    def rob_linear(houses):
        prev, curr = 0, 0
        for money in houses:
            prev, curr = curr, max(prev + money, curr)
        return curr
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
nums = [2, 3, 2]
print(rob_houses(nums))  

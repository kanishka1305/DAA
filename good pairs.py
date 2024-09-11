# Good Pairs Counter

def numIdenticalPairs(nums):
    count = 0
    num_count = {}
    
    for num in nums:
        if num in num_count:
            count += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1
            
    return count

# Example usage
nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))  # Output: 4

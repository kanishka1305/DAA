from itertools import combinations

def meet_in_the_middle(arr, target):
    n = len(arr)
    mid = n // 2
    
    # Split the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Generate all possible subset sums for both halves
    left_sums = {sum(comb) for r in range(len(left_half) + 1) for comb in combinations(left_half, r)}
    right_sums = {sum(comb) for r in range(len(right_half) + 1) for comb in combinations(right_half, r)}
    
    # Find the closest sum to the target
    closest_sum = float('inf')
    for left_sum in left_sums:
        for right_sum in right_sums:
            current_sum = left_sum + right_sum
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                
    return closest_sum

# Example usage
set_a = [45, 34, 4, 12, 5, 2]
target_a = 42
result_a = meet_in_the_middle(set_a, target_a)
print(f"Closest sum to {target_a} in set A: {result_a}")

set_b = [1, 3, 2, 7, 4, 6]
target_b = 10
result_b = meet_in_the_middle(set_b, target_b)
print(f"Closest sum to {target_b} in set B: {result_b}")

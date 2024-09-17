def meet_in_the_middle(arr, target_sum):
    from itertools import combinations

    n = len(arr)
    mid = n // 2

    # Generate all possible subset sums for the first half
    left_sums = set()
    for i in range(mid + 1):
        for combo in combinations(arr[:mid], i):
            left_sums.add(sum(combo))

    # Generate all possible subset sums for the second half
    right_sums = set()
    for i in range(n - mid + 1):
        for combo in combinations(arr[mid:], i):
            right_sums.add(sum(combo))

    # Check if there exists a pair of sums that add up to the target sum
    for left in left_sums:
        if (target_sum - left) in right_sums:
            return True

    return False

# Test cases
E1 = [1, 3, 9, 2, 7, 12]
exact_sum1 = 15
print(meet_in_the_middle(E1, exact_sum1))  # Output: True

E2 = [3, 34, 4, 12, 5, 2]
exact_sum2 = 15
print(meet_in_the_middle(E2, exact_sum2))  # Output: True

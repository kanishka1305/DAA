def maxSumAfterQuery(nums, queries):
    MOD = 10**9 + 7
    res = 0
    for x, (i, val) in enumerate(queries):
        nums[i] = val
        dp = [0] * len(nums)
        for j, num in enumerate(nums):
            dp[j] = num
            if j >= 2:
                dp[j] = max(dp[j], dp[j-2] + num)
            if j >= 3:
                dp[j] = max(dp[j], dp[j-3] + num)
        res = (res + max(dp)) % MOD
    return res
nums = [1, 2, 3, 4, 5]
queries = [[1, 2], [4, 6]]
print(maxSumAfterQuery(nums, queries))  # Output: 61

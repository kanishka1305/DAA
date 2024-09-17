def median_of_medians(arr, k):
    if len(arr) == 0:
        return None
    if len(arr) < 10:
        return sorted(arr)[k - 1]
    sublists = [arr[j:j + 5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians) // 2 + 1)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    k_index = len(low)
    if k_index == k - 1:
        return pivot
    elif k - 1 < k_index:
        return median_of_medians(low, k)
    else:
        return median_of_medians(high, k - k_index - 1)
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print(median_of_medians(arr1, k1))

arr2 = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27]
k2 = 5
print(median_of_medians(arr2, k2))

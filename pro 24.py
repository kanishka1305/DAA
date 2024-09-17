def find_min_max(arr):
    # Check if the array is empty
    if not arr:
        return None, None
    # The minimum value is the first element
    min_value = arr[0]
    # The maximum value is the last element
    max_value = arr[-1]
    return min_value, max_value

# Test cases
# Input: N=8, a[] = [2, 4, 6, 8, 10, 12, 14, 18]
arr1 = [2, 4, 6, 8, 10, 12, 14, 18]
min1, max1 = find_min_max(arr1)
print(f"Input: N=8, a[] = {arr1} => Min = {min1}, Max = {max1}")

# Input: N=9, a[] = [11, 13, 15, 17, 19, 21, 23, 35, 37]
arr2 = [11, 13, 15, 17, 19, 21, 23, 35, 37]
min2, max2 = find_min_max(arr2)
print(f"Input: N=9, a[] = {arr2} => Min = {min2}, Max = {max2}")

# Input: N=10, a[] = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
arr3 = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
min3, max3 = find_min_max(arr3)
print(f"Input: N=10, a[] = {arr3} => Min = {min3}, Max = {max3}")

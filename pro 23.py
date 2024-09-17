def find_min_max(arr):
    # Initialize min and max with the first element of the array
    min_value = arr[0]
    max_value = arr[0]
    
    # Iterate through the array to find min and max
    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
            
    return min_value, max_value

# Test cases
# Input: N= 8, a[] = {5,7,3,4,9,12,6,2}
arr1 = [5, 7, 3, 4, 9, 12, 6, 2]
min1, max1 = find_min_max(arr1)
print(f"Min = {min1}, Max = {max1}")

# Input: N= 9, a[] = {1,3,5,7,9,11,13,15,17}
arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
min2, max2 = find_min_max(arr2)
print(f"Min = {min2}, Max = {max2}")

# Input: N= 10, a[] = {22,34,35,36,43,67,12,13,15,17}
arr3 = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
min3, max3 = find_min_max(arr3)
print(f"Min = {min3}, Max = {max3}")

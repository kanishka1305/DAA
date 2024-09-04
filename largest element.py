def largest_element(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("The largest element is:", largest_element(array))

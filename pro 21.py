def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test Cases
# Input: N= 8, a[] = {31,23,35,27,11,21,15,28}
arr1 = [31, 23, 35, 27, 11, 21, 15, 28]
merge_sort(arr1)
print(arr1)  # Output: [11, 15, 21, 23, 27, 28, 31, 35]

# Input: N= 10, a[] = {22,34,25,36,43,67, 52,13,65,17}
arr2 = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
merge_sort(arr2)
print(arr2)  # Output: [13, 17, 22, 25, 34, 36, 43, 52, 65, 67]

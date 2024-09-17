def merge_sort(arr, comparisons=0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the elements into 2 halves
        R = arr[mid:]

        comparisons += merge_sort(L, comparisons)  # Sorting the first half
        comparisons += merge_sort(R, comparisons)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            comparisons += 1  # Increment comparison count
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return comparisons

# Test cases
arr1 = [12, 4, 78, 23, 45, 67, 89, 1]
comparisons1 = merge_sort(arr1)
print(f"Sorted array: {arr1}, Comparisons: {comparisons1}")

arr2 = [38, 27, 43, 3, 9, 82, 10]
comparisons2 = merge_sort(arr2)
print(f"Sorted array: {arr2}, Comparisons: {comparisons2}")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
input_array = [5, 2, 9, 1, 5, 6]
sorted_array = selection_sort(input_array)
print("Sorted Output:", sorted_array)

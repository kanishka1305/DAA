def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_array = insertion_sort(input_array)
print(sorted_array)  

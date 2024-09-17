def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
input_data = [4, 3, 5, 1]
sorted_data = insertion_sort(input_data)
print(sorted_data)  

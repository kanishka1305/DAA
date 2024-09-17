def bubble_sort_best_case(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
input_data_best = [1, 2, 3, 4, 5]
output_data_best = bubble_sort_best_case(input_data_best)
print(output_data_best)  

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    print(f"Pivot: {pivot}, Less: {less_than_pivot}, Greater: {greater_than_pivot}")
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
array = [10, 16, 8, 12, 15, 6, 3, 9, 5]
sorted_array = quick_sort(array)
print("Sorted Array:", sorted_array)

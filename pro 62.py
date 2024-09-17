def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        print(f"Array after partitioning with pivot {pivot}: {left + middle + right}")
        return quick_sort(left) + middle + quick_sort(right)
array = [19, 72, 35, 46, 58, 91, 22, 31]
print("Initial array:", array)
sorted_array = quick_sort(array)
print("Sorted array:", sorted_array)

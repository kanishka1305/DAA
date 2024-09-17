def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    steps = []
    while left <= right:
        mid = left + (right - left) // 2
        steps.append(f"Mid-point calculation: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == key:
            return mid, steps
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps
a = [3, 9, 14, 19, 25, 31, 42, 47, 53]
search_key = 31
position, calculations = binary_search(a, search_key)

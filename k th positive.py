# Kth Positive Integer Missing from Sorted Array

def findKthPositive(arr, k):
    missing_count = 0
    current = 1
    index = 0
    
    while missing_count < k:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

# Example usage
arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  # Output: 9

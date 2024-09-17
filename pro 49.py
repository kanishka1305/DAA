def max_weight(weights, max_capacity):
    weights.sort(reverse=True)
    total_weight = 0
    for weight in weights:
        if total_weight + weight <= max_capacity:
            total_weight += weight
    return total_weight
n = 5
weights = [10, 20, 30, 40, 50]
max_capacity = 60
output = max_weight(weights, max_capacity)
print(output)  
